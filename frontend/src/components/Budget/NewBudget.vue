<template lang="html">
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
									<input type="number" name="total_planeado" class="form-control" v-model.trin="form.total_planeado">
								</div>
							</div>

							<div class="form-group row">
								<label for="total_actual" class="col-sm-2 col-form-label">Total Actual</label>
								<div class="col-sm-6">
									<input type="number" name="total_actual" class="form-control" v-model.trin="form.total_actual">
								</div>
							</div>

							<div class="form-group row">
								<label for="tipo" class="col-sm-2 col-form-label">Tipo</label>
								<div class="col-sm-6">
									<input type="text"  name="tipo" class="form-control" v-model.trin="form.tipo">
								</div>
							</div>

							<div class="form-group row">
								<label for="estado" class="col-sm-2 col-form-label">Estado</label>
								<div class="col-sm-6">
									<input type="text" name="estado" class="form-control" v-model.trin="form.estado">
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
</template>

<script>
	import axios from 'axios'
	import swal from 'sweetalert'
	export default {
		data(){
			return{
				form: {
					nombre: '',
					saldo: '',
					tipo:'',
					estado:''
				}
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
					this.form.tipo = response.data.tipo
					this.form.estado = response.data.estado
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
	
</style>