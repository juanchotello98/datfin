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
					<h2>Crear Cuenta</h2>
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
									<label for="saldo" class="col-sm-2 col-form-label">Saldo</label>
									<div class="col-sm-6">
										<input type="number" name="saldo" class="form-control" v-model.trin="form.saldo">
									</div>
								</div>

								<div class="form-group row">
									<label for="tipo" class="col-sm-2 col-form-label">Tipo</label>
									<div class="col-sm-6">
	    								<b-form-select v-model="form.tipo" :options="tipos"></b-form-select>
	    							</div>
								</div>

								<div class="form-group row">
									<label for="estado" class="col-sm-2 col-form-label">Estado</label>
							  		<div class="col-sm-6">
	    								<b-form-select v-model="form.estado" :options="estados"></b-form-select>
	    							</div>
								</div>

								<div class="rows">
									<div class="col text-left">
										<b-button type="submit" variant="primary">Crear</b-button>
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
				tipos:[
				{ value: 'debito', text:'debito' },
				{ value: 'credito', text:'credito' }
				],
				estados:[
				{ value: 'activa', text:'activa' },
				{ value: 'inactiva', text:'inactiva' }
				],
				form: {
					nombre: '',
					saldo: '',
					tipo:'',
					estado:''
				}
			}
		},

		methods: {
			onSubmit(evt){
				evt.preventDefault()
				const path = 'http://localhost:8000/api/v1.0/accounts/'
				axios.post(path, this.form).then((response) => {
					this.form.nombre = response.data.nombre
					this.form.saldo = response.data.saldo
					this.form.tipo = response.data.tipo
					this.form.estado = response.data.estado
					
					swal("Cuenta creado exitosamente","","success")
				})
				.catch((error) => {
					swal("La cuenta no ha sido creada","","error")
				})

			},

		},
		created(){
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