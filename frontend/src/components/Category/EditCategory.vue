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
								<label for="tipo" class="col-sm-2 col-form-label">Tipo</label>
								<div class="col-sm-6">
									<input type="number"  name="tipo" class="form-control" v-model.trin="form.planeado">
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
</template>

<script>
	import axios from 'axios'
	import swal from 'sweetalert'
	export default {
		data(){
			return{
				budgetId: this.$route.params.budgetId,
				categoryId: this.$route.params.categoryId,
				form: {
					nombre: '',
					planeado: ''
				}
			}
		},

		methods: {
			onSubmit(evt){
				evt.preventDefault()
				const path = 'http://localhost:8000/api/v1.0/categories/'+this.categoryId+'/'
				axios.put(path, this.form).then((response) => {
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

			},

			getCategory(){
				const path = 'http://localhost:8000/api/v1.0/categories/'+this.categoryId+'/'
				axios.get(path).then((response) => {
					this.form.nombre = response.data.nombre
					this.form.planeado = response.data.planeado
					this.form.actual = response.data.actual
					this.form.diferencia = response.data.diferencia
					this.form.presupuesto = response.data.presupuesto
				})
				.catch((error) => {
					console.log(error)
				}) 
			}
		},
		created(){
			this.getCategory()
		}
	}	
</script>

<style lang="css" scoped>
	
</style>