<template>
  <div>
    <!-- Cabecera del sitio -->
    <headerNav />

    <!-- Título de la sección centrado -->
    <div class="institutions_table_title" style="text-align: center; margin: 20px 0;">
      <h1>Bancos</h1>
    </div>

    <!-- Contenedor para la tabla de bancos, ajustando el ancho -->
    <div class="institutions_container_table" style="display: flex; justify-content: center;">
      <div class="institutions_table" style="width: 90%;"> <!-- Cambiar el ancho aquí -->
        <!-- Tabla usando a-table -->
        <a-table
          :loading="loading"
          :dataSource="institutions"
          rowKey="id"
          @rowClick="account"
          bordered
          style="width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);"
        >
          <a-table-column title="ID" dataIndex="id" key="id" />
          <a-table-column title="Nombre" dataIndex="name" key="name" width="250" />
          <a-table-column title="Estado" dataIndex="status" key="status" />
          <a-table-column title="País" dataIndex="country_codes" key="country_codes" />
          <a-table-column title="Integración" dataIndex="integration_type" key="integration_type" width="250" />
          <a-table-column title="Tipo" dataIndex="type" key="type" />
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
      tableData: [this.institutions],
      loading : true
    }
  },
    computed:{
        ...mapState('institution',['institutions'])
    },
    components: {
      headerNav
    },
    async mounted () {
        await this.init()
        this.loading = false
    },
    methods:{
        ...mapActions('institution',['getInstitutions']),
      async init(){
        await this.getInstitutions()
        //this.loading = true
      },
      async account(row, column, cell, even){
        //console.log(row.id)
        //console.log(row.name)
        this.$router.push({ path: `/account/${row.name}`})
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