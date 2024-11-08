const user = {
    store: {
        user: null,
    },
    actions: {
        async addUser(datos) {
            try {
                const response = await this.$axios.post('users', datos);
            } catch (error) {
                console.log(error)
                this.$message.error(`${error.response.data}`);
            }
        },
    },
};

export const state =() => ({
    ...user.store
});

export const actions = {
    ...user.actions
};

