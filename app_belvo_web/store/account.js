const account = {
    store: {
        account: null,
        accounts: [],
    },
    actions: {
        async getAccounts({ commit } ) {
            try {
                const {data} = await this.$axios.get('account');
                await commit("setAcccounts", data.data);
            } catch (error) {
                console.log(error)
                this.$message.error(`${error.response.data}`);
            }
        },

        async getAccountsForInstitution({ commit },institution_name ) {
            try {
                const {data} = await this.$axios.get(`account?institution_name=${institution_name}`);
                await commit("setAcccounts", data.data);
            } catch (error) {
                console.log(error)
                this.$message.error(`${error.response.data}`);
            }
        },
        //async getInstituttion(datos) {
        //    try {
        //        const response = await this.$axios.post('institutions', datos);
        //    } catch (error) {
        //        console.log(error)
        //        this.$message.error(`${error.response.data}`);
        //    }
        //},
    },
    mutations:{
        setAcccounts: (state, payload) => (state.accounts = payload),
    }
};

export const state =() => ({
    ...account.store
});

export const actions = {
    ...account.actions
};
export const mutations = {
    ...account.mutations
};

