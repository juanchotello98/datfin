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
					<h2>Editar Presupuesto</h2>
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

								<div class="rows">
									<div class="col text-left">
										<b-button type="submit" variant="primary">Editar</b-button>
										<b-button type="submit" class="btn-large-space" :to="{ name: 'ListBudget' }">Cancelar</b-button>
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
				budgetId: this.$route.params.budgetId,
				form: {

					nombre: ''
				}
			}
		},

		methods: {
			onSubmit(evt){
				evt.preventDefault()
				const path = 'http://localhost:8000/api/v1.0/budgets/'+this.budgetId+'/'
				axios.put(path, this.form).then((response) => {
					this.form.mes = response.data.mes
					this.form.nombre = response.data.nombre
					this.form.total_planeado = response.data.total_planeado
					this.form.total_actual = response.data.total_actual
					swal("Presupuesto actualizado exitosamente","","success")
				})
				.catch((error) => {
					console.log(error)
				})

			},

			getBudget(){
				const path = 'http://localhost:8000/api/v1.0/budgets/'+this.budgetId+'/'
				axios.get(path).then((response) => {
					this.form.mes = response.data.mes
					this.form.nombre = response.data.nombre
					this.form.total_planeado = response.data.total_planeado
					this.form.total_actual = response.data.total_actual
				})
				.catch((error) => {
					console.log(error)
				}) 
			}
		},
		created(){
			this.getBudget()
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