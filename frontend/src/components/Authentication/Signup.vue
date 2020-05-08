<template lang="html">
  <div>
    <div>
      </div>
    <div class="container">
      <div class="row">
        <div class="col text-left">
          <h2 id="title"><b-icon icon="graph-up"></b-icon> &nbsp;Bienvenido a DATFIN </h2>
        </div>  
      </div>
      <div class="row">
        <div class="col">
          <div id="my-card" class="card">
            <div id="my-card-body" class="card-body">
              <form class="login form" @submit="onSubmit">

                <div class="form-group row">
                  <label id="my-label" for="username" class="col-sm-6 col-form-label"><b>Usuario</b></label>
                  <input type="text" v-model="form.username" name="username" class="form-control">
                </div>

                <div class="form-group row">
                  <label id="my-label" for="password" class="col-sm-6 col-form-label"><b>Contraseña</b></label>
                  <input type="password" name="password" class="form-control" v-model="form.password">
                </div>

                <div class="form-group row">
                  <label id="my-label" for="first_name" class="col-sm-6 col-form-label"><b>Nombres</b></label>
                  <input type="text" name="first_name" class="form-control" v-model="form.first_name">
                </div>

                <div class="form-group row">
                  <label id="my-label" for="last_name" class="col-sm-6 col-form-label"><b>Apellidos</b></label>
                  <input type="text" name="last_name" class="form-control" v-model="form.last_name">
                </div>

                <div class="form-group row">
                  <label id="my-label" for="email" class="col-sm-6 col-form-label"><b>Email</b></label>
                  <input type="text" name="email" class="form-control" v-model="form.email">
                </div>

                <div class="rows">
                  <div id="login" class="col text-left">
                    <b-button  type="submit" variant="success">Sign up</b-button>
                    <b-button variant="secondary" :to="{ name: 'Login' }">Log in</b-button>
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
        form: {
          username: '',
          password: '',
          first_name: '',
          last_name:'',
          email:''
        }
      }
    },

    methods: {
      onSubmit(evt){
        evt.preventDefault()
        const path = 'https://appdatfin.herokuapp.com/api/v1.0/users/'
        axios.post(path, this.form).then((response) => {
          swal("Usuario registrado exitosamente","","success")
        })
        .catch((error) => {
          swal("El usurario no pudo ser registrado","","error")
          console.log(error)
        })

      },
    },
    created(){
    }
  } 
</script>
<style lang="css">
    #my-card{
    margin-right: 410px;
    margin-left: 350px;
    }

    #my-card-body{
    margin-left: 8px;
    margin-right: 8px;
    }

    #login{
      margin-left: 55px;
    }

    #title{
    margin-left: 350px;
    margin-top: 30px
    }

    #my-label{
      text-align: left;
    }
</style>