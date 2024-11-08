const transaction = {
    store: {
        transaction: null,
        transactions: [],
        balance: null,
    },
    actions: {
        async getTransactions({ commit }, ) {
            try {
                const {data} = await this.$axios.get('transactions');
                await commit("setTransactions", data.data);
            } catch (error) {
                console.log(error)
                this.$message.error(`${error.response.data}`);
            }
        },
        async getTransactionsForAccount({ commit },account_id ) {
            try {
                const {data} = await this.$axios.get(`transactions?account_id=${account_id}`);
                await commit("setTransactions", data.data);
                await commit("setBalance", data.balance.toFixed(2));
            } catch (error) {
                console.log(error)
                this.$message.error(`${error.response.data}`);
            }
        },
    },
    mutations:{
        setTransactions: (state, payload) => (state.transactions = payload),
        setBalance: (state, payload) => (state.balance = payload),
    }
};

export const state =() => ({
    ...transaction.store
});

export const actions = {
    ...transaction.actions
};
export const mutations = {
    ...transaction.mutations
};

