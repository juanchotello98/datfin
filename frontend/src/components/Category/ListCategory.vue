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
						<h2>Listado de Categorias </h2>
						<b-button size="sm" :to="{name: 'NewCategory'}" variant="primary" >Crear Categorias</b-button>
						<b-button size="sm" :to="{name: 'ListBudget'}" variant="secondary" >Volver</b-button>
						<b-button size="sm" variant="success" v-on:click="set" >Actualizar</b-button>
					</div>
					<br>
				</div>
				<div class="col-md-12">
					<b-table class="my-table" small id="my-table" striped hover :items="categories" :fields="fields"  :per-page="perPage" :current-page="currentPage" default>
						<template v-slot:cell(action)="data">
							<b-button size="sm" variant="primary" :to="{ name: 'EditCategory', params: { categoryId: data.item.id } }">Editar</b-button>
							<b-button size="sm" variant="danger" :to="{ name: 'DeleteCategory', params: { categoryId: data.item.id } }">Eliminar</b-button>
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
				userId : this.$store.state.authUser[0].id,
				firstName : this.$store.state.authUser[0].first_name,
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
				presupuesto: [],
				perPage: 5,
        		currentPage: 1,
        		new_pnombre:'',
        		new_mes:'',
        		new_total_planeado:0,
        		new_total_actual:0,
        		new_pusuario:''

			}
		},
    	computed: {
      		rows() {
        		return this.categories.length
      		},
    	},
		methods: {
    		signOut(){
    			this.$store.commit("removeToken")
    			this.$router.push({name: 'Login'})
    		},
			getCategories(){
				const path = 'https://appdatfin.herokuapp.com/api/v1.0/categories/?presupuesto='+this.budgetId
				console.log(path)
				axios.get(path,  {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					this.categories = response.data.results
				})
				.catch((error) => {
					console.log(error)
				})
			},
			getBudget(){
				const path = 'https://appdatfin.herokuapp.com/api/v1.0/budgets/'+this.budgetId+'/'
				axios.get(path,  {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					this.presupuesto = response.data
				})
				.catch((error) => {
					console.log(error)
				}) 
			},
			set: function(event){
				this.new_total_actual = 0;
				for(var i=0; i < this.categories.length; i++){
					this.new_total_actual = this.new_total_actual + this.categories[i].actual
				}
				this.new_total_planeado = this.presupuesto.total_planeado
				this.new_mes = this.presupuesto.mes
				this.new_pnombre = this.presupuesto.nombre
				this.new_pusuario = this.presupuesto.usuario

				const path = 'https://appdatfin.herokuapp.com/api/v1.0/budgets/'+this.budgetId+'/'
				let config = {
						"mes" : this.new_mes,
						"nombre" : this.new_pnombre,
        				"total_planeado" : this.new_total_planeado,
        				"total_actual"  : this.new_total_actual,
        				"usuario" : this.new_pusuario
				};
				axios.put(path, config,  {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					console.log(response)
					swal("Actualizadas exitosamente","","success")
				})
				.catch((error) => {
					console.log(error)
				})
			},
		},

		created(){
			this.getCategories()
			this.getBudget()
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
