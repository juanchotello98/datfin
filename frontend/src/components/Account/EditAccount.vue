<template lang="html">
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
								<label for="nombre" class="col-sm-2 col-form-label">Nombre</label>
								<div class="col-sm-6">
									<input type="text" name="nombre" class="form-control" v-model.trin="form.nombre">
								</div>
							</div>


							
							<div class="form-group row">
								<label for="tipo" class="col-sm-2 col-form-label">Tipo</label>
								<div class="col-sm-6">
									<input type="text"  name="tipo" class="form-control" v-model.trin="form.tipo">
								</div>
							</div>

							<div class="form-group row">
								<label for="estado" class="col-sm-2 col-form-label">Estado</label>
								<div class="col-sm-6">
									<input type="text"  name="estado" class="form-control" v-model.trin="form.estado">
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
</template>

<script>
	import axios from 'axios'
	import swal from 'sweetalert'
	export default {
		data(){
			return{
				accountId: this.$route.params.accountId,
				form: {
					nombre: '',
					tipo: '',
					estado:''
				}
			}
		},

		methods: {
			onSubmit(evt){
				evt.preventDefault()
				const path = 'http://localhost:8000/api/v1.0/accounts/'+this.accountId+'/'
				axios.put(path, this.form).then((response) => {
					this.form.nombre = response.data.nombre
					this.form.saldo = response.data.saldo
					this.form.tipo = response.data.tipo
					this.form.estado = response.data.estado
					swal("Cuenta actualizada exitosamente","","success")
				})
				.catch((error) => {
					console.log(error)
				})

			},

			getAccount(){
				const path = 'http://localhost:8000/api/v1.0/accounts/'+this.accountId+'/'
				axios.get(path).then((response) => {
					this.form.nombre = response.data.nombre
					this.form.saldo = response.data.saldo
					this.form.tipo = response.data.tipo
					this.form.estado = response.data.estado
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
	
</style>