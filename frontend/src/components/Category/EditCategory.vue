<template lang="html">
	<div>
    	<div>
      		<b-navbar class="my-navar" toggleable="lg" type="dark" variant="primary">
        		<b-navbar-brand><b-icon icon="graph-up"></b-icon> DATFIN</b-navbar-brand>
        		<b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
          			<b-navbar-nav class="ml-auto">
            			<b-nav-item-dropdown right>
              				<template v-slot:button-content>
                				<em>¡Hola!&nbsp;{{firstName}}</em>
              				</template>
              			<b-dropdown-item v-on:click="signOut">Sign Out</b-dropdown-item>
            			</b-nav-item-dropdown>
          			</b-navbar-nav>
        		</b-collapse>
      		</b-navbar>
    	</div>
		<div>
	    <b-sidebar id="sidebar-no-header" aria-labelledby="sidebar-no-header-title" no-header visible width="250px" shadow>
	    	<template v-slot:default="{ hide }">
	        	<div class="p-3">
	          		<h4 id="sidebar-no-header-title"><b-icon icon="graph-up"></b-icon> &nbsp;DATFIN</h4>
	          		<nav class="mb-3">
	            		<b-nav vertical>
	            			<b-button class="btn" variant="primary" :to="{name: 'HelloWorld'}" block><b-icon icon="house-fill"></b-icon>&nbsp;&nbsp;Inicio</b-button>
	              			<b-button class="btn" variant="primary" :to="{name: 'ListAccount'}" block><b-icon icon="credit-card"></b-icon>&nbsp;&nbsp;Cuentas</b-button>
	              			<b-button class="btn" variant="primary" :to="{name: 'ListBudget'}" block><b-icon icon="wallet"></b-icon> &nbsp;Presupuestos</b-button>
                      		<b-button class="btn" variant="primary" :to="{name: 'ListTransaction'}" block><b-icon icon="arrow-left-right"></b-icon> &nbsp;Transacciones</b-button>	              			
	            		</b-nav>
	          		</nav>
	        	</div>
	      	</template>
	    </b-sidebar>
	  	</div>
		<div class="container">
			<div class="row">
				<div class="col text-left">
					<h2>Editar Categoria {{ set }} </h2>					
				</div>	
			</div>

			<div class="row">
				<div class="col">
					<div class="card">
						<div class="card-body">
							<form @submit="onSubmit">
								
								<div class="form-group row">
									<label for="nombre" class="col-sm-2 col-form-label">Nombre</label>
									<div class="col-sm-6">
										<input type="text" name="nombre" class="form-control" v-model.trin="form.nombre">
									</div>
								</div>

								<div class="form-group row">
									<label for="planeado" class="col-sm-2 col-form-label">Planeado</label>
									<div class="col-sm-6">
										<input type="number"  name="planeado" class="form-control" v-model.trin="form.planeado">
									</div>
								</div>

								<div class="form-group row">
									<label for="actual" class="col-sm-2 col-form-label">Actual</label>
									<div class="col-sm-6">
										<input type="number" disabled="true" name="actual" class="form-control" v-model.trin="form.actual">
									</div>
								</div>

								<div class="form-group row">
									<label for="diferencia" class="col-sm-2 col-form-label">Diferencia</label>
									<div class="col-sm-6">
										<input type="text" disabled="true" name="diferencia" class="form-control" v-model.trin="form.diferencia=form.planeado-form.actual">
									</div>
								</div>

								<div class="rows">
									<div class="col text-left">
										<b-button type="submit" variant="primary">Editar</b-button>
										<b-button type="submit" class="btn-large-space" :to="{ name: 'ListCategory', params: { budgetd: budgetId   } }">Cancelar</b-button>
									</div>
								</div>

							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import axios from 'axios'
	import swal from 'sweetalert'
	export default {
		data(){
			return{
				userId : this.$store.state.authUser[0].id,
				firstName : this.$store.state.authUser[0].first_name,
				form_put: {
					put_mes:'',
					put_nombre:'',
					put_total_planeado: 0,
					put_total_actual: 0,
					put_usuario:'',
					put_diferencia: 0
				},
				budgetId: this.$route.params.budgetId,
				categoryId: this.$route.params.categoryId,
				form: {
					nombre: '',
					planeado: ''
				},
				categories: [], 
				presupuesto:[], 
				categoria:[]
			}
		},
		computed:{
			set: function(){
				this.form_put.put_total_planeado = 0;
				for(var i=0; i < this.categories.length; i++){
					this.form_put.put_total_planeado = this.form_put.put_total_planeado + this.categories[i].planeado
				}
				this.form_put.put_diferencia = this.categoria.planeado - this.form.planeado
				if (this.form.planeado < this.categoria.planeado  ){
					this.form_put.put_total_planeado = this.form_put.put_total_planeado  - this.form_put.put_diferencia 
				}else if(this.form.planeado === this.categoria.planeado ){
					this.form_put.put_total_planeado = this.form_put.put_total_planeado
				}else if(this.form.planeado > this.categoria.planeado){
					this.form_put.put_total_planeado = this.form_put.put_total_planeado + this.form_put.put_diferencia*-1
				}
				this.form_put.put_mes = this.presupuesto.mes
				this.form_put.put_nombre = this.presupuesto.nombre
				this.form_put.put_total_actual = this.presupuesto.total_actual
				this.form_put.put_usuario = this.presupuesto.usuario
			}
		},
		methods: {
    		signOut(){
    			this.$store.commit("removeToken")
    			this.$router.push({name: 'Login'})
    		},
			onSubmit(evt){
				evt.preventDefault()
				const path = 'https://appdatfin.herokuapp.com/api/v1.0/categories/'+this.categoryId+'/'
				axios.put(path, this.form, {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					this.form.nombre = response.data.nombre
					this.form.planeado = response.data.planeado
					this.form.actual = response.data.actual
					this.form.diferencia = response.data.diferencia
					this.form.presupuesto = response.data.presupuesto
					swal("Categoria actualizada exitosamente","","success")
				})
				.catch((error) => {
					console.log(error)
				})
				this.updateBudget()

			},
			getCategory(){
				const path = 'https://appdatfin.herokuapp.com/api/v1.0/categories/'+this.categoryId+'/'
				axios.get(path, {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					this.categoria = response.data
					this.form.nombre = response.data.nombre
					this.form.planeado = response.data.planeado
					this.form.actual = response.data.actual
					this.form.diferencia = response.data.diferencia
					this.form.presupuesto = response.data.presupuesto
				})
				.catch((error) => {
					console.log(error)
				}) 
			},
			getCategories(){
				const path = 'https://appdatfin.herokuapp.com/api/v1.0/categories/?presupuesto='+this.budgetId
				console.log(path)
				axios.get(path, {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					this.categories = response.data.results
				})
				.catch((error) => {
					console.log(error)
				})
			},
			getBudget(){
				const path = 'https://appdatfin.herokuapp.com/api/v1.0/budgets/'+this.budgetId+'/'
				axios.get(path, {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					this.presupuesto = response.data
				})
				.catch((error) => {
					console.log(error)
				}) 
			},
			updateBudget(){
				const path = 'https://appdatfin.herokuapp.com/api/v1.0/budgets/'+this.budgetId+'/'
				let config = {
						"mes": this.form_put.put_mes,
        				"nombre": this.form_put.put_nombre,
        				"total_planeado": this.form_put.put_total_planeado,
        				"total_actual": this.form_put.put_total_actual,
        				"usuario": this.form_put.put_usuario
				};
				axios.put(path, config, {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					console.log(response)
				})
				.catch((error) => {
					console.log(error)
				})
			}
		},
		created(){
			this.getCategory()
			this.getCategories()
			this.getBudget()
		}
	}	
</script>

<style lang="css" scoped>
	.container{
		margin-left: 270px;
		margin-top: 30px;
	}
	.card{
		width: 900px;
	}
	.btn{
		text-align: left;
	}
  	.my-navar{
    	margin-left: 250px;
  	}
</style>