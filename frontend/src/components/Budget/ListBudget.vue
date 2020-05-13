<template lang="html">
	<div>
    	<div>
      		<b-navbar class="my-navar" toggleable="lg" type="dark" variant="primary">
        		<b-navbar-brand><b-icon icon="graph-up"></b-icon> DATFIN</b-navbar-brand>
        		<b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
          			<b-navbar-nav class="ml-auto">
            			<b-nav-item-dropdown right>
              				<template v-slot:button-content>
                				<em>¡Hola!&nbsp;{{firstName}}</em>
              				</template>
              			<b-dropdown-item v-on:click="signOut">Sign Out</b-dropdown-item>
            			</b-nav-item-dropdown>
          			</b-navbar-nav>
        		</b-collapse>
      		</b-navbar>
    	</div>
		<div>
	    <b-sidebar id="sidebar-no-header" aria-labelledby="sidebar-no-header-title" no-header visible width="250px" shadow>
	    	<template v-slot:default="{ hide }">
	        	<div class="p-3">
	          		<h4 id="sidebar-no-header-title"><b-icon icon="graph-up"></b-icon> &nbsp;DATFIN</h4>
	          		<nav class="mb-3">
	            		<b-nav vertical>
	            			<b-button class="btn" variant="primary" :to="{name: 'HelloWorld'}" block><b-icon icon="house-fill"></b-icon>&nbsp;&nbsp;Inicio</b-button>
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
					<div>
						<h2>Listado de Presupuestos</h2>
						<b-button size="sm" :to="{name: 'NewBudget'}" variant="primary" >Crear Presupuesto</b-button>
					</div>
					<br>
				</div>
				<div v-if="budgets.length===0" class="col-md-12">
					<b-spinner variant="primary" label="Spinning"></b-spinner>
					<span class="primary">Cargando...</span>
				</div>
				<div v-else class="col-md-12">
					<b-table class="my-table" small id="my-table" striped hover :items="budgets" :fields="fields" :per-page="perPage" :current-page="currentPage" default>
						<template v-slot:cell(action)="data">
							<b-button size="sm" variant="primary" :to="{ name: 'EditBudget', params: { budgetId: data.item.id } }">Editar</b-button>
							<b-button size="sm" variant="danger" :to="{ name: 'DeleteBudget', params: { budgetId: data.item.id } }">Eliminar</b-button>							
							<b-button size="sm" variant="secondary" :to="{ name: 'ListCategory', params: { budgetId: data.item.id } }">Ver Categorias</b-button>
							<b-button size="sm" variant="success" :to="{ name: 'NewCategory', params: { budgetId: data.item.id } }">Crear Categorias</b-button>
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
				firstName : this.$store.state.authUser[0].first_name,
				userId : this.$store.state.authUser[0].id,
				fields: [
				{ key: 'id', label: 'ID'},
				{ key: 'mes', label: 'Fecha'},
				{ key: 'nombre', label:'Nombre' },
				{ key: 'total_planeado', label: 'Planeado'},
				{ key: 'total_actual', label:'Actual' },
				{ key: 'action', label: ''}
				],
				budgets: [],
				perPage: 5,
        		currentPage: 1,
			}
		},
    	computed: {
      		rows() {
        		return this.budgets.length
      		}
    	},
		methods: {
    		signOut(){
    			this.$store.commit("removeToken")
    			this.$router.push({name: 'Login'})
    		},
			getBudgets(){
				const path = 'https://appdatfin.herokuapp.com/api/v1.0/budgets/?usuario='+this.userId
				axios.get(path,  {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					this.budgets = response.data.results
				})
				.catch((error) => {
					console.log(error)
				})
			}
		},

		created(){
			this.getBudgets()
		}
	}
</script>

<style lang="css" scoped>
	.container{
		margin-left: 270px;
		margin-top: 30px;
	}
	.my-table{
		width: 1050px;
	}
	.btn{
		text-align: left;
	}
  	.my-navar{
    	margin-left: 250px;
  	}
</style>
