<template>
  <div>
    <!-- Cabecera del sitio -->
    <headerNav />

    <!-- Título y balance -->
    <div class="institutions_table_title">
      <a-page-header @back="goBack" title="Volver"></a-page-header>

      <!-- Mostrar el balance de forma centrada -->
      <div class="balance-container">
        <table class="balance-table">
          <tr>
            <th class="balance-title">BALANCE</th>
            <td class="balance-amount">{{ balance }}</td>
          </tr>
        </table>
      </div>

      <!--div class="balance-title">
        <h1>BALANCE : {{ balance }}</h1>
      </div-->
    </div>

    <!-- Contenedor de la tabla -->
    <div class="institutions_container_table">
      <div class="institutions_table">
        <a-table :loading="loading" :dataSource="transactions" rowKey="id" bordered 
          style="min-width: 800px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);"
          >
          <a-table-column title="ID" dataIndex="id" key="id" />
          <a-table-column title="Categoria" dataIndex="category" key="category" width="200" />
          <a-table-column title="Descripcion" dataIndex="description" key="description" width="250" />
          <a-table-column title="Estado" dataIndex="status" key="status" width="200" />
          <a-table-column title="Tipo" dataIndex="type" key="type" width="150" />
          <a-table-column title="Moneda" dataIndex="currency" key="currency" width="150" />
          <a-table-column title="Balance" dataIndex="balance" key="balance" width="150" />
          <a-table-column title="Cantidad" dataIndex="amount" key="amount" width="150" />
        </a-table>
      </div>
    </div>
  </div>
</template>

  
  <script>
  import {mapState,mapActions,mapMutations} from 'vuex';
  import headerNav from '~/components/headerNav.vue';
  export default {
    name: 'IndexPage',
      data() {
      return {
        tableData: [this.transactions],
        loading : true
      }
    },
      computed:{
          ...mapState('transaction',['transactions','balance'])
      },
      components: {
        headerNav
      },
      async mounted () {
          this.init()
      },
      methods:{
          ...mapActions('transaction',['getTransactionsForAccount']),
        async init(){
          await this.getTransactionsForAccount(this.$route.params.slug)
          this.loading = false
        },
        goBack() {
          this.$router.go(-1)
        },
        async logout() {
          // Lógica de cierre de sesión
          await this.$auth.logout()
          localStorage.removeItem('authToken'); // Eliminar el token de autenticación
          this.$router.push('/login'); // Redirigir a la página de inicio de sesión
        }
      }
  }
  </script>
  <style scoped></style>