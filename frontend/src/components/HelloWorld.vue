<template>
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
    <div id="inicio">
      <h2>
        <i>Bienvenido a DATFIN, aquí puedes registrar cuentas, registrar prespuestos y asignarles categorias y también puedes registrar transacciones con base en tus cuentas y presupuestos.</i>
      </h2>
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
  </div>
</template>

<script>
export default {
  data () {
    return {
      userId : this.$store.state.authUser[0].id,
      firstName : this.$store.state.authUser[0].first_name,
    }
  },
  computed:{
  },
  methods:{
    signOut(){
      this.$store.commit("removeToken")
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .btn{
    text-align: left;
  }
  .my-navar{
    margin-left: 250px;
  }
  #my-chart{
    margin-left: 300px;
    margin-top: 30px;
  }
  #inicio{
    margin-left: 300px;
    margin-top: 200px;
  }
</style>
