<template lang="html">
	<div>
		<div>
	    <b-sidebar id="sidebar-no-header" aria-labelledby="sidebar-no-header-title" no-header visible width="250px" shadow>
	    	<template v-slot:default="{ hide }">
	        	<div class="p-3">
	          		<h4 id="sidebar-no-header-title"><b-icon icon="graph-up"></b-icon> &nbsp;DATFIN</h4>
	          		<nav class="mb-3">
	            		<b-nav vertical>
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
					<h2>Crear Ingreso {{set}} </h2>
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
									<label for="tipo" class="col-sm-2 col-form-label">Tipo</label>
									<div class="col-sm-6">
										<input type="text" disabled="true" name="tipo" class="form-control" v-model.trin="form.tipo">
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
									<label for="categoria" class="col-sm-2 col-form-label">Categoria</label>
									<div class="col-sm-6">
										<input type="text" placeholder="no-aplica" disabled="true" name="categoria" class="form-control" v-model.trin="form.categoria">
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
				form: {
					fecha: '',
					descripcion: '',
					valor:0,
					tipo:'ingreso',
					cuenta:'',
					categoria: 27
				},
				cuentas:[],
				categorias:[],

				new_saldo: 0,
				mew_nombre:'',
				new_tipo:'',
				new_estado:'',

				new_cnombre:'',
				new_planeado:0,
				new_actual:0,
				new_diferencia:0,
				new_presupuesto:''
			}
		},
		computed:{
			set: function(){
				for(var i=0; i < this.cuentas.length; i++){
					if(this.cuentas[i].id===parseInt(this.form.cuenta)){
						this.new_saldo = parseInt(this.cuentas[i].saldo) + parseInt(this.form.valor)
						this.new_nombre =  this.cuentas[i].nombre
						this.new_tipo =  this.cuentas[i].tipo
						this.new_estado =  this.cuentas[i].estado
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
		},
		methods: {
			onSubmit(evt){
				evt.preventDefault()
				const path = 'http://localhost:8000/api/v1.0/transactions/'
				axios.post(path, this.form).then((response) => {
					this.form.fecha = response.data.fecha
					this.form.descripcion = response.data.descripcion
					this.form.valor = response.data.valor
					this.form.tipo = response.data.tipo
					this.form.cuenta = response.data.cuenta
					this.form.categoria = response.data.categoria
					
					swal("Ingreso creado exitosamente","","success")
				})
				.catch((error) => {
					swal("El ingreso no ha sido creado","","error")
				})
				this.updateAccount()
				//this.updateCategory()
			},
			getAccounts(){
				const path = 'http://localhost:8000/api/v1.0/accounts/'
				axios.get(path).then((response) => {
					this.cuentas = response.data
				})
				.catch((error) => {
					console.log(error)
				})
			},
			getCategories(){

				const path = 'http://localhost:8000/api/v1.0/categories/'
				console.log(path)
				axios.get(path).then((response) => {
					this.categorias = response.data
				})
				.catch((error) => {
					console.log(error)
				})
			},	
			updateAccount(){
				const path = 'http://localhost:8000/api/v1.0/accounts/'+this.form.cuenta+'/'
				let config = {
						"nombre": this.new_nombre,
        				"saldo": this.new_saldo,
        				"tipo": this.new_tipo,
        				"estado": this.new_estado
				};
				axios.put(path, config).then((response) => {
					console.log(response)
				})
				.catch((error) => {
					console.log(error)
				})

			},
			updateCategory(){
				const path = 'http://localhost:8000/api/v1.0/categories/'+this.form.categoria+'/'
				let config = {
						"nombre" : this.new_cnombre,
        				"planeado" : this.new_planeado,
        				"actual"  : this.new_actual,
        				"diferencia" : this.new_diferencia,
        				"presupuesto" : this.new_presupuesto
				};
				axios.put(path, config).then((response) => {
					console.log(response)
				})
				.catch((error) => {
					console.log(error)
				})
			},
		},
		created(){
			this.getAccounts()
			this.getCategories()
		}
	}	
</script>

<style lang="css" scoped>
	.container{
		margin-left: 270px;
	}

	.card{
		width: 900px;
	}
	.btn{
		text-align: left;
	}
</style>