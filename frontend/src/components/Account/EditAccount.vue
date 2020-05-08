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
					<h2>Editar Cuenta</h2>
				</div>	
			</div>

			<div class="row">
				<div class="col">
					<div class="card">
						<div class="card-body">
							<form @submit="onSubmit">
								
								<div class="form-group row">
									<label for="saldo" class="col-sm-2 col-form-label">Saldo</label>
									<div class="col-sm-6">
										<input type="number" disabled="true" name="saldo" class="form-control" v-model.trin="form.saldo">
									</div>
								</div>

								<div class="form-group row">
									<label for="nombre" class="col-sm-2 col-form-label">Nombre</label>
									<div class="col-sm-6">
										<input type="text" name="nombre" class="form-control" v-model.trin="form.nombre">
									</div>
								</div>

								<div class="rows">
									<div class="col text-left">
										<b-button type="submit" variant="primary">Editar</b-button>
										<b-button type="submit" class="btn-large-space" :to="{ name: 'ListAccount' }">Cancelar</b-button>
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
				userId : this.$store.state.authUser[0].id,
				firstName : this.$store.state.authUser[0].first_name,
				accountId: this.$route.params.accountId,
				form: {
					nombre: '',
					saldo:''
				}
			}
		},

		methods: {
    		signOut(){
    			this.$store.commit("removeToken")
    			this.$router.push({name: 'Login'})
    		},
			onSubmit(evt){
				evt.preventDefault()
				const path = 'https://appdatfin.herokuapp.com/api/v1.0/accounts/'+this.accountId+'/'
				axios.put(path, this.form,  {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					this.form.nombre = response.data.nombre
					this.form.saldo = response.data.saldo
					this.form.tipo = response.data.tipo
					swal("Cuenta actualizada exitosamente","","success")
				})
				.catch((error) => {
					console.log(error)
				})

			},

			getAccount(){
				const path = 'https://appdatfin.herokuapp.com/api/v1.0/accounts/'+this.accountId+'/'
				axios.get(path,  {'headers': {'Authorization' : 'JWT ' + this.$store.state.jwt}}).then((response) => {
					this.form.nombre = response.data.nombre
					this.form.saldo = response.data.saldo
					this.form.tipo = response.data.tipo
				})
				.catch((error) => {
					console.log(error)
				}) 
			}
		},
		created(){
			this.getAccount()
		}
	}	
</script>

<style lang="css" scoped>
	.container{
		margin-left: 270px;
		margin-top: 30px;
	}
	.card{
		width: 900px;
	}
	.btn{
		text-align: left;
	}
  	.my-navar{
    	margin-left: 250px;
  	}
</style>