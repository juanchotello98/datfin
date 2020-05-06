<template lang="html">
  <div>
    <div>
      </div>
    <div class="container">
      <div class="row">
        <div class="col text-left">
          <h2 id="title"><b-icon icon="graph-up"></b-icon> &nbsp;Bienvenido a DATFIN</h2>
        </div>  
      </div>
      <div class="row">
        <div class="col">
          <div id="my-card" class="card">
            <div id="my-card-body" class="card-body">
              <form class="login form">
                <div class="form-group row">
                  <label id="my-label" for="username" class="col-sm-6 col-form-label"><b>Usuario</b></label>
                  <input type="text" v-model="username" name="username" class="form-control">
                </div>

                <div class="form-group row">
                  <label id="my-label" for="password" class="col-sm-6 col-form-label"><b>Contraseña</b></label>
                  <input type="password" name="password" class="form-control" v-model="password">
                </div>

                <div class="rows">
                  <div id="login" class="col text-left">
                    <b-button @click.prevent="authenticate" type="submit" variant="success">Log in</b-button>
                    <b-button variant="secondary" :to="{ name: 'Signup' }">Sign up</b-button>
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

export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    authenticate () {
      const payload = {
        username: this.username,
        password: this.password
      }
      axios.post(this.$store.state.endpoints.obtainJWT, payload)
        .then((response) => {
          this.$store.commit('updateToken', response.data.token)
          // get and set auth user
          const base = {
            baseURL: this.$store.state.endpoints.baseUrl,
            headers: {
            // Set your Authorization to 'JWT', not Bearer!!!
              Authorization: 'JWT ' + this.$store.state.jwt,
              'Content-Type': 'application/json'
            },
            xhrFields: {
                withCredentials: true
            }
          }
          // Even though the authentication returned a user object that can be
          // decoded, we fetch it again. This way we aren't super dependant on
          // JWT and can plug in something else.
          const axiosInstance = axios.create(base)
          axiosInstance({
            //url: "/users/",
            url:"/users/?username="+this.username,
            method: "get",
            params: {}
          })
            .then((response) => {
              this.$store.commit("setAuthUser",
                {authUser: response.data.results, isAuthenticated: true}
              )
              this.$router.push({name: 'HelloWorld'})
            })

        })
        .catch((error) => {
          swal("El usuario  no existe, por favor regístrate","","error")
          console.log(error);
          console.debug(error);
          console.dir(error);
        })
    }
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