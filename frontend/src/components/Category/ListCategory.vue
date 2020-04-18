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
					<div>
						<h2>Listado de Categorias</h2>
						<b-button size="sm" :to="{name: 'NewCategory'}" variant="primary" >Crear Categorias</b-button>
						<b-button size="sm" :to="{name: 'ListBudget'}" variant="secondary" >Volver</b-button>
					</div>
					<br>
				</div>
				<div class="col-md-12">
					<b-pagination
						align="center"
      					v-model="currentPage"
      					:total-rows="rows"
      					:per-page="perPage"
      					aria-controls="my-table"
    				></b-pagination>
					<b-table class="my-table" small id="my-table" striped hover :items="categories" :fields="fields"  :per-page="perPage" :current-page="currentPage" default>
						<template v-slot:cell(action)="data">
							<b-button size="sm" variant="primary" :to="{ name: 'EditCategory', params: { categoryId: data.item.id } }">Editar</b-button>
						</template>
					</b-table>
					<b-pagination
						align="center"
      					v-model="currentPage"
      					:total-rows="rows"
      					:per-page="perPage"
      					aria-controls="my-table"
    				></b-pagination>
				</div>		
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
				categories: [],
				perPage: 5,
        		currentPage: 1,
			}
		},
    	computed: {
      		rows() {
        		return this.categories.length
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

<style lang="css" scoped>
	.container{
		margin-left: 270px;
	}
	.my-table{
		width: 1050px;
	}
	.btn{
		text-align: left;
	}
</style>
