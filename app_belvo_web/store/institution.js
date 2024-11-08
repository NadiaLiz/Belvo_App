const institution = {
    store: {
        institution: null,
        institutions: [],
    },
    actions: {
        async getInstitutions({ commit } ) {
            try {
                const {data} = await this.$axios.get('institutions');
                console.log(data)
                await commit("setInstitutions", data.data);
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
        setInstitutions: (state, payload) => (state.institutions = payload),
    }
};

export const state =() => ({
    ...institution.store
});

export const actions = {
    ...institution.actions
};
export const mutations = {
    ...institution.mutations
};

