<template lang="html">
	<div class="container">

		<div class="row">
			<div class="col text-left">
				<h2>Editar Presupuestos</h2>
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
								<label for="estado" class="col-sm-2 col-form-label">Estado</label>
								<div class="col-sm-6">
									<input type="text" disabled="true" name="estado" class="form-control" v-model.trin="form.estado=selectedstate">
								</div>
						  		<div class="col-sm-1">
    								<b-form-radio v-model="selectedstate" name="some-radios-" value="activa">activa</b-form-radio>
    							</div>
						  		<div class="col-xs-5">
    								<b-form-radio v-model="selectedstate" name="some-radios-" value="inactiva">inactiva</b-form-radio>
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
</template>

<script>
	import axios from 'axios'
	import swal from 'sweetalert'
	export default {
		data(){
			return{
				budgetId: this.$route.params.budgetId,
				selectedstate: '',
				form: {

					nombre: '',
					estado: ''
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
					this.form.estado = response.data.estado
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
					this.form.tipo = response.data.tipo
					this.form.total_planeado = response.data.total_planeado
					this.form.total_actual = response.data.total_actual
					this.form.tipo = response.data.tipo
					this.form.estado = response.data.estado
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
	
</style>