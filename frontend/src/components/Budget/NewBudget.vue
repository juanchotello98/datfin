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
					<h2>Crear Presupuesto</h2>
				</div>	
			</div>

			<div class="row">
				<div class="col">
					<div class="card">
						<div class="card-body">
							<form @submit="onSubmit">

								<div class="form-group row">
									<label for="mes" class="col-sm-2 col-form-label">Fecha</label>
									<div class="col-sm-6">
										<input type="date" name="mes" class="form-control" v-model.trin="form.mes">
									</div>
								</div>
								
								<div class="form-group row">
									<label for="nombre" class="col-sm-2 col-form-label">Nombre</label>
									<div class="col-sm-6">
										<input type="text" name="nombre" class="form-control" v-model.trin="form.nombre">
									</div>
								</div>
								
								<div class="form-group row">
									<label for="total_planeado" class="col-sm-2 col-form-label">Total Planeado</label>
									<div class="col-sm-6">
										<input type="number" disabled="true" name="total_planeado" class="form-control" v-model.trin="form.total_planeado=initial">
									</div>
								</div>

								<div class="form-group row">
									<label for="total_actual" class="col-sm-2 col-form-label">Total Actual</label>
									<div class="col-sm-6">
										<input type="number" disabled="true" name="total_actual" class="form-control" v-model.trin="form.total_actual=initial">
									</div>
								</div>

								<div class="rows">
									<div class="col text-left">
										<b-button type="submit" variant="primary">Crear</b-button>
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
				form: {
					mes: '',
					nombre: '',
					total_planeado:'',
					total_actual:''
				}
			}
		},
		computed:{
			initial: function(){
				var initial = 0;
				return initial
			}
		},
		methods: {
			onSubmit(evt){
				evt.preventDefault()
				const path = 'http://localhost:8000/api/v1.0/budgets/'
				axios.post(path, this.form).then((response) => {
					this.form.mes = response.data.mes
					this.form.nombre = response.data.nombre
					this.form.total_planeado = response.data.total_planeado
					this.form.total_actual = response.data.total_actual
					swal("Presupuesto creado exitosamente","","success")
				})
				.catch((error) => {
					swal("La cuenta no ha sido creada","","error")
				})

			},

		},
		created(){
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