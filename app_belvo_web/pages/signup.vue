<template lang="">
    <div class="login_container_page">
        <div class="login_container_form">
            <div class="login_form">
              <div class="form-title">
                 Registrarse
              </div>
                <a-form :layout="formState.layout" :model="formState" v-bind="formItemLayout" class="demo-form-inline">
                    <a-form-item label="Correo Electronico"  class="form-item-label">
                      <a-input v-model:value="formState.email" placeholder="Correo Electronico" />
                    </a-form-item>
                    <a-form-item label="Password" class="form-item-label">
                      <a-input v-model:value="formState.password" placeholder="Password" />
                    </a-form-item>
                    <a-form-item :wrapper-col="vertical">
                      <a-button @click="onSubmit" type="primary" class="login-button">Registrarse</a-button>
                    </a-form-item>
                    </a-form>
                    <div class="create-account-link">
                      <span>¿Ya tienes una cuenta?</span>
                      <a @click="backToLogin" type="primary"  class="signup-link">Iniciar sesión</a>
                    </div>
                    

            </div>
        </div>
    </div>
</template>
<script>

import { signin } from '~/common/constants';

export default {
    auth: false,
    data() {
        return {
            loading: false,
            //formState: {
            //    email: "prueba@gmail.com",
            //    password: "prueba"
            //},
            formState: {
                email: "",
                password: ""
            },
            form: { ...signin.form },
            error: ''
        }

    },
    methods: {
        backToLogin() {
            this.$router.push('/login')
        },
        async onSubmit() {

            try {
                this.loading = true;
                this.form.companyname = this.form.institute
                await this.$axios.post('signup', this.formState).then(res => {
                    this.$message.success("Usuario creado con exito", 4)
                    this.clear();
                    this.$router.push('/');
                }).catch(error => {
                    this.$message.error(error.response.data, 3)
                })
            } finally {
                this.loading = false;
            }
            this.clear();
            this.$router.push('login')
        },
        clear() {
            this.form = signin.form;
        }

    }
}
</script>
<style>
</style>