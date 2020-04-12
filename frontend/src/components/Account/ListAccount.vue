<template lang="html">
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
				<b-table striped hover :items="accounts" :fields="fields">
					<template v-slot:cell(action)="data">
						<b-button size="sm" variant="primary" :to="{ name: 'EditAccount', params: { accountId: data.item.id } }">Editar</b-button>
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
				{ key: 'saldo', label: 'Saldo'},
				{ key: 'tipo', label:'Tipo' },
				{ key: 'estado', label:'Estado' },
				{ key: 'action', label: ''}
				],
				accounts: []
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

<style lang="css" scoped></style>
