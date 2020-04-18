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
	            		</b-nav>
	          		</nav>
	        	</div>
	      	</template>
	    </b-sidebar>
	  	</div>
		<div class="container">
			<div class="row">
				<div class="col text-left">
					<h2>Editar Categoria</h2>
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