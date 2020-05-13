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
					<h2>Crear Egreso {{set}} {{set_dos}} {{set_tres}}</h2>
				</div>	
			</div>
			<div class="row">
				<div class="col">
					<div class="card">
						<div class="card-body">
							<form @submit="onSubmit">

								<div class="form-group row">
									<label for="fecha" class="col-sm-2 col-form-label">Fecha</label>
									<div class="col-sm-6">
										<input type="date" name="fecha" class="form-control" v-model.trin="form.fecha">
									</div>
								</div>
								
								<div class="form-group row">
									<label for="descripcion" class="col-sm-2 col-form-label">Descripcion</label>
									<div class="col-sm-6">
										<input type="text" name="descripcion" class="form-control" v-model.trin="form.descripcion">
									</div>
								</div>
								
								<div class="form-group row">
									<label for="valor" class="col-sm-2 col-form-label">Valor</label>
									<div class="col-sm-6">
										<input type="number" name="valor" class="form-control" v-model.trin="form.valor">
									</div>
								</div>								

								<div class="form-group row">
									<label for="categoria" class="col-sm-2 col-form-label">Cuenta</label>
							  		<div class="col-sm-6">
	    				        		<select v-model="form.cuenta" class="form-control" id="cuenta">
            								<option v-for="cuenta in cuentas" :value="cuenta.id">{{cuenta.nombre}} ({{ cuenta.saldo }})</option>
        								</select>
        							
	    							</div>
								</div>

								<div class="form-group row">
									<label for="presupuesto" class="col-sm-2 col-form-label">Presupuesto</label>
							  		<div class="col-sm-6">
	    				        		<select @change="getCategories($event)" v-model="form.presupuesto" class="form-control" id="presupuesto">
            								<option v-for="presupuesto in presupuestos" :value="presupuesto.id">{{presupuesto.nombre}}</option>
        								</select>
        							
	    							</div>
								</div>

								<div class="form-group row">
									<label for="categoria" class="col-sm-2 col-form-label">Categoria</label>
							  		<div class="col-sm-6">
	    				        		<select v-model="form.categoria" class="form-control" id="categoria">
            								<option v-for="categoria in categorias" :value="categoria.id">{{categoria.nombre}}</option>
        								</select>
	    							</div>
								</div>

								<div class="rows">
									<div class="col text-left">
										<b-button type="submit" variant="primary">Crear</b-button>
										<b-button type="submit" class="btn-large-space" :to="{ name: 'ListTransaction' }">Cancelar</b-button>
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
				firstName : this.$store.state.authUser[0].first_name,
				userId : this.$store.state.authUser[0].id,
				form: {
					fecha: '',
					descripcion: '',
					valor:0,
					tipo:'',
					cuenta:'',
					presupuesto:'',
					categoria:'',
					usuario: ''
				},
				cuentas:[],
				presupuestos:[],
				categorias:[],

				new_saldo: 0,
				mew_nombre:'',
				new_tipo:'',

				new_cnombre:'',
				new_planeado:'',
				new_actual:'',
				new_diferencia:'',
				new_presupuesto:'',

				pnew_total_actual:'',
				pnew_total_planeado:'',
				pnew_mes:'',
				pnew_pnombre:'',
				pnew_pusuario:''
			}
		},
		computed:{
			set: function(){
				for(var i=0; i < this.cuentas.length; i++){
					if(this.cuentas[i].id===parseInt(this.form.cuenta)){
						this.new_saldo = parseInt(this.cuentas[i].saldo) - parseInt(this.form.valor)
						this.new_nombre =  this.cuentas[i].nombre
						this.new_tipo =  this.cuentas[i].tipo
						this.form.usuario = this.userId
						this.form.tipo = 'Egreso'
					}
				}
			},
			set_dos: function(){
				for(var i=0; i < this.categorias.length; i++){
					if(this.categorias[i].id===parseInt(this.form.categoria)){
						this.new_actual = parseInt(this.categorias[i].actual) + parseInt(this.form.valor)
						this.new_diferencia = this.categorias[i].planeado - this.new_actual
						this.new_cnombre =  this.categorias[i].nombre
						this.new_planeado =  this.categorias[i].planeado
						this.new_presupuesto =  this.categorias[i].presupuesto
					}
				}
			},
			set_tres: function(){
				for(var i=0; i < this.presupuestos.length; i++){
					if(this.presupuestos[i].id===parseInt(this.form.presupuesto)){
						this.pnew_total_actual = parseInt(this.presupuestos[i].total_actual) + parseInt(this.form.valor)
						this.pnew_total_planeado = this.presupuestos[i].total_planeado
						this.pnew_mes = this.presupuestos[i].mes
						this.pnew_pnombre = this.presupuestos[i].nombre
						this.pnew_pusuario = this.presupuestos[i].usuario
					}
				}
			}
		},
		methods: {
    		signOut(){
    			this.$store.commit("removeToken")
    			this.$router.push({name: 'Login'})
    		},
			onSubmit(evt){
				evt.preventDefault()
				const path = 'https://appdatfin.herokuapp.com/api/v1.0/transactions/'
				axios.post(path, this.form, {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					this.form.fecha = response.data.fecha
					this.form.descripcion = response.data.descripcion
					this.form.valor = response.data.valor
					this.form.tipo = response.data.tipo
					this.form.cuenta = response.data.cuenta
					this.form.categoria = response.data.categoria
					
					swal("Egreso creado exitosamente","","success")
				})
				.catch((error) => {
					swal("El egreso no ha sido creado","","error")
				})
				this.updateAccount()
				this.updateBudget()
				this.updateCategory()
			},
			getAccounts(){
				const path = 'https://appdatfin.herokuapp.com/api/v1.0/accounts/?usuario='+this.userId
				axios.get(path, {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					this.cuentas = response.data.results
				})
				.catch((error) => {
					console.log(error)
				})
			},
			getBudgets(){
				const path = 'https://appdatfin.herokuapp.com/api/v1.0/budgets/?usuario='+this.userId
				axios.get(path,  {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					this.presupuestos = response.data.results
				})
				.catch((error) => {
					console.log(error)
				})
			},
			getCategories(event){

				const path = 'https://appdatfin.herokuapp.com/api/v1.0/categories/?presupuesto='+event.target.value
				console.log(path)
				axios.get(path, {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					this.categorias = response.data.results
				})
				.catch((error) => {
					console.log(error)
				})
			},	
			updateAccount(){
				const path = 'https://appdatfin.herokuapp.com/api/v1.0/accounts/'+this.form.cuenta+'/'
				let config = {
						"nombre": this.new_nombre,
        				"saldo": this.new_saldo,
        				"tipo": this.new_tipo
				};
				axios.put(path, config, {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					console.log(response)
				})
				.catch((error) => {
					console.log(error)
				})

			},
			updateCategory(){
				const path = 'https://appdatfin.herokuapp.com/api/v1.0/categories/'+this.form.categoria+'/'
				let config = {
						"nombre" : this.new_cnombre,
        				"planeado" : this.new_planeado,
        				"actual"  : this.new_actual,
        				"diferencia" : this.new_diferencia,
        				"presupuesto" : this.new_presupuesto
				};
				axios.put(path, config, {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					console.log(response)
				})
				.catch((error) => {
					console.log(error)
				})
			},
			updateBudget(){
				const path = 'https://appdatfin.herokuapp.com/api/v1.0/budgets/'+this.form.presupuesto+'/'
				let config = {
						"mes" : this.pnew_mes,
        				"nombre" : this.pnew_pnombre,
        				"total_planeado"  : this.pnew_total_planeado,
        				"total_actual" : this.pnew_total_actual,
        				"usuario" : this.pnew_pusuario
				};
				axios.put(path, config, {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					console.log(response)
				})
				.catch((error) => {
					console.log(error)
				})
			},
		},
		created(){
			this.getAccounts()
			this.getBudgets()
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