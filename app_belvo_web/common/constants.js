
export const signin = {
    form: {
        username: "",
        password: ""
    },
    rules: {
        username: [
            { required: true, message: "El nombre de usuario es requerido" }
        ],
        password: [
            { required: true, message: "La contraseña es requerida" },
            // {
            //     min: 6,
            //     message: "La contraseña debe tener al menos 6 caracteres"
            // }
        ]
    }
};
