<template lansg="html">
	<div class="container">
		<div class="row">
			<div class="col text-left">
				<div>
					<h2>Listado de Categorias</h2>
					<b-button size="sm" :to="{name: 'NewCategory'}" variant="primary" >Crear Categorias</b-button>
					<b-button size="sm" :to="{name: 'ListBudget'}" variant="secondary" >Volver</b-button>
				</div>
				<br>
			</div>
			<div class="col-md-12">
				<b-table striped hover :items="categories" :fields="fields">
					<template v-slot:cell(action)="data">
						<b-button size="sm" variant="primary" :to="{ name: 'EditCategory', params: { categoryId: data.item.id } }">Editar</b-button>
					</template>
				</b-table>
			</div>
			
		</div>
	</div>
	
</template>

<script>
	import axios from 'axios'
	export default {
		data(){
			return {
				budgetId: this.$route.params.budgetId,
				fields: [
				{ key: 'id', label: 'ID'},
				{ key: 'nombre', label:'Nombre' },
				{ key: 'planeado', label: 'Planeado'},
				{ key: 'actual', label:'Actual' },
				{ key: 'diferencia', label:'Diferencia' },
				{ key: 'presupuesto', label:'Presupuesto' },
				{ key: 'action', label: ''}
				],
				categories: []
			}
		},
		methods: {
			getCategories(){

				const path = 'http://localhost:8000/api/v1.0/categories/?presupuesto='+this.budgetId
				console.log(path)
				axios.get(path).then((response) => {
					this.categories = response.data
				})
				.catch((error) => {
					console.log(error)
				})
			}
		},

		created(){
			this.getCategories()
		}
	}
</script>

<style lang="css" scoped></style>
