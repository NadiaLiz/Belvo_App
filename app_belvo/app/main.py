from fastapi import FastAPI
from app.routes import user_routes  # , auth_routes
from app.routes.transactions_routes import transaction_router
from app.routes.institutions_routes import institucion_router
from app.routes.accounts_routes import account_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# @app.get("/")
# def index():
#    return {"menssage": "saludos"}


#
#
# @app.post("/users")
# def index():
#    return "saludos"
# app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(user_routes.router, prefix="/api")
app.include_router(transaction_router, prefix="/api")
app.include_router(institucion_router, prefix="/api")
app.include_router(account_router, prefix="/api")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],   # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],   # Permitir todos los encabezados
)