<template>
  <div>
    <!-- Header con fondo blanco y sombra sutil -->
    <a-layout-header class="header">
      <div style="display: flex; justify-content: space-between; width: 100%; align-items: center;">
        
        <!-- Logo a la izquierda -->
        <div style="display: flex; align-items: center;">
          <img src="@/css/images/Belvo.png" alt="Logo" class="logo_header" style="height: 40px; margin-right: 10px;" />
          
        </div>
        
        <!-- Botón de cerrar sesión a la derecha -->
        <div 
        style="display:flex; width:50%; color: #4a4a4a !important; justify-content: end; align-items: center; cursor: pointer;" @click="logout">
          Cerrar Sesión
        </div>
      </div>
    </a-layout-header>
  </div>
</template>
  
  <script>
  
    export default {
    methods:{
            async logout() {
            // Lógica de cierre de sesión
            await this.$auth.logout()
            localStorage.removeItem('authToken'); // Eliminar el token de autenticación
            this.$router.push('/login'); // Redirigir a la página de inicio de sesión
            }
        }
    }

  </script>