<template lang="">
    <div class="login_container_page">
        <div class="login_container_form">
            <div class="login_form">
                <div class="logo-container">
                    <img src="@/css/images/Belvo.png" alt="Logo" class="logo"/>
                </div>
                <a-form :layout="formState.layout" :model="formState" class="demo-form-inline">
                    <a-form-item label="Correo Electronico"  class="form-item-label"  >
                      <a-input v-model:value="formState.email" placeholder="Correo Electronico" prefix-icon="mail" />
                    </a-form-item>
                    <a-form-item label="Password" class="form-item-label">
                      <a-input type="password" v-model:value="formState.password" placeholder="Password" prefix-icon="lock" />
                    </a-form-item>
                    <a-form-item >
                      <a-button @click="onSubmit" type="primary" class="login-button">Ingresar</a-button>
                    </a-form-item>
                    </a-form>
                    <div class="create-account-link">
                      <span>¿No tienes una cuenta?</span>
                      <a @click="signup" type="primary" class="signup-link">Registrate</a>
                    </div>

            </div>
        </div>
    </div>
</template>
<script>
import { signin } from '~/common/constants';

export default {
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
        signup(){
            this.$router.push('/signup')
        },
        async onSubmit() {

            try {
                this.loading = true,
                await this.$auth.login({ data: this.formState })
                    .then((response) => {
                        console.log("saludos mensaje correcto")
                        console.log(response)
                        this.$message.success('Bienvenido', 3)
                    })
                    .catch((e) => {
                        if (!e.response) {
                            console.log("e.response")
                            console.log(e.response)
                            this.$message.error('Error: Network Error');
                        } else {
                            console.log("saludos mensaje")
                            this.$message.error(`${e.response.data}`);
                            this.clear();
                        }
                    })
            } finally {
                this.loading = false
            }
            this.clear();
            this.$router.push('/')
        },
    clear(){
      this.form = signin.form;
    }

    }
}
</script>
<style>
</style>