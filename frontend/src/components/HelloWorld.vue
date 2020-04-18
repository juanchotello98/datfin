<template>
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
  </div>
</template>

<script>
export default {
  data () {
    return {
    
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .btn{
    text-align: left;
  }
</style>
