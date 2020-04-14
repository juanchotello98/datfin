<template lang="html">
	<div class="container">

		<div class="row">
			<div class="col text-left">
				<h2>Crear Categoria</h2>
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
								<label for="total_planeado" class="col-sm-2 col-form-label">Planeado</label>
								<div class="col-sm-6">
									<input type="number" name="total_planeado" class="form-control" v-model.trin="form.planeado">
								</div>
							</div>

							<div class="form-group row">
								<label for="total_actual" class="col-sm-2 col-form-label">Actual</label>
								<div class="col-sm-6">
									<input type="number" name="total_actual" class="form-control" v-model.trin="form.actual">
								</div>
							</div>

							<div class="form-group row">
								<label for="tipo" class="col-sm-2 col-form-label">Diferencia</label>
								<div class="col-sm-6">
									<input type="text"  name="tipo" class="form-control" v-model.trin="form.diferencia">
								</div>
							</div>

							<div class="form-group row">
								<label for="estado" class="col-sm-2 col-form-label">Presupuesto</label>
								<div class="col-sm-6">
									<input type="text" name="estado" class="form-control" v-model.trin="form.presupuesto">
								</div>
							</div>


							<div class="rows">
								<div class="col text-left">
									<b-button type="submit" variant="primary">Crear</b-button>
									<b-button type="submit" class="btn-large-space" :to="{ name: 'ListCategory', params: { budgetd: budgetId   } }">Cancelar</b-button>
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
				form: {
					id: '',
					nombre: '',
					planeado: '',
					actual:'',
					diferencia:'',
					presupuesto:''
				}
			}
		},

		methods: {
			onSubmit(evt){
				evt.preventDefault()
				const path = 'http://localhost:8000/api/v1.0/categories/'
				axios.post(path, this.form).then((response) => {
					this.form.nombre = response.data.nombre
					this.form.planeado = response.data.planeado
					this.form.actual = response.data.actual
					this.form.diferencia = response.data.diferencia
					this.form.presupuesto = response.data.presupuesto
					swal("Categoria creada exitosamente","","success")
				})
				.catch((error) => {
					swal("La categoria no ha sido creada","","error")
				})

			},

		},
		created(){
		}
	}	
</script>

<style lang="css" scoped>
	
</style>