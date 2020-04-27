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
						<h2>Listado de Cuentas</h2>
						<b-button size="sm" :to="{name: 'NewAccount'}" variant="primary" >Crear Cuenta</b-button>
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
					<b-table class="my-table" small striped hover :items="accounts" :fields="fields" :per-page="perPage" :current-page="currentPage" default>
						<template v-slot:cell(action)="data">
							<b-button size="sm" variant="primary" :to="{ name: 'EditAccount', params: { accountId: data.item.id } }">Editar</b-button>
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
				fields: [
				{ key: 'id', label: 'ID'},
				{ key: 'nombre', label:'Nombre' },
				{ key: 'saldo', label: 'Saldo'},
				{ key: 'tipo', label:'Tipo' },
				{ key: 'estado', label:'Estado' },
				{ key: 'action', label: ''}
				],
				accounts: [],
				perPage: 5,
        		currentPage: 1,
			}
		},
    	computed: {
      		rows() {
        		return this.accounts.length
      		}
    	},
		methods: {
			getAccounts(){
				const path = 'http://localhost:8000/api/v1.0/accounts/'
				axios.get(path).then((response) => {
					this.accounts = response.data
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
