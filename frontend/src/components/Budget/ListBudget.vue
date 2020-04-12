<template lang="html">
	<div class="container">
		<div class="row">
			<div class="col text-left">
				<div>
					<h2>Listado de Presupuestos</h2>
					<b-button size="sm" :to="{name: 'NewBudget'}" variant="primary" >Crear Presupuesto</b-button>
				</div>
				<br>
			</div>
			<div class="col-md-12">
				<b-table striped hover :items="budgets" :fields="fields">
					<template v-slot:cell(action)="data">
						<b-button size="sm" variant="primary" :to="{ name: 'EditBudget', params: { budgetId: data.item.id } }">Editar</b-button>
						<b-button size="sm" variant="secondary" :to="{ name: 'ListCategory', params: { budgetId: data.item.id } }">Ver Categorias</b-button>
						<b-button size="sm" variant="success" :to="{ name: '', params: { budgetId: data.item.id } }">Crear Categorias</b-button>
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
				fields: [
				{ key: 'id', label: 'ID'},
				{ key: 'nombre', label:'Nombre' },
				{ key: 'total_planeado', label: 'Planeado'},
				{ key: 'total_actual', label:'Actual' },
				{ key: 'action', label: ''}
				],
				budgets: []
			}
		},
		methods: {
			getAccounts(){
				const path = 'http://localhost:8000/api/v1.0/budgets/'
				axios.get(path).then((response) => {
					this.budgets = response.data
				})
				.catch((error) => {
					console.log(error)
				})
			}
		},

		created(){
			this.getAccounts()
		}
	}
</script>

<style lang="css" scoped></style>
