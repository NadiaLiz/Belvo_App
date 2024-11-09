<template>
  <div>
    <!-- Cabecera del sitio -->
    <headerNav />

    <!-- Título de la sección centrado -->
    <div class="institutions_table_title">
      <a-page-header @back="goBack" title="Volver"></a-page-header>

      <!-- Mostrar el balance de forma centrada -->
      <div class="institutions_table_title_" style="text-align: center; margin: 20px 0;">
        <h1>Cuentas</h1>
      </div>
    </div>
   
    <!-- Contenedor para la tabla de cuentas centrada y con mayor ancho -->
    <div class="institutions_container_table" style="display: flex; justify-content: center;">
      <div class="institutions_table" style="width: 90%;"> <!-- Ajuste del ancho aquí -->
        <!-- Tabla usando a-table -->
        <a-table
          :loading="loading"
          :dataSource="accounts"
          rowKey="number"
          @rowClick="redirectTransaction"
          bordered
          style="min-width: 800px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);"
        >
          <a-table-column title="Agencia" dataIndex="agency" key="agency" />
          <a-table-column title="Categoria" dataIndex="category" key="category" width="200" />
          <a-table-column title="Moneda" dataIndex="currency" key="currency" />
          <a-table-column title="Nombre" dataIndex="name" key="name" width="200" />
          <a-table-column title="Numero" dataIndex="number" key="number" />
          <a-table-column title="Tipo" dataIndex="type" key="type" width="180" />
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
        tableData: [this.accounts],
        loading : true
      }
    },
      computed:{
          ...mapState('account',['accounts'])
      },
      components: {
        headerNav
      },
      async mounted () {
          this.init()
          this.loading = false
      },
      methods:{
          ...mapActions('account',['getAccountsForInstitution']),
        async init(){
          await this.getAccountsForInstitution(this.$route.params.slug)
          console.log(this.accounts[0])
        },
        async redirectTransaction(row, column, cell, even){
          //console.log(row.id)
          //console.log(row.name)
          this.$router.push({ path: `/transaction/${row.id}`})
        },
        goBack() {
          this.$router.go(-1)
        },
        logout() {
          // Lógica de cierre de sesión
          localStorage.removeItem('authToken'); // Eliminar el token de autenticación
          this.$router.push('/login'); // Redirigir a la página de inicio de sesión
        }
      }
  }
  </script>
  <style scoped></style>