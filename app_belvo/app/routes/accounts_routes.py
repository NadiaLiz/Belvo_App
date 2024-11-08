from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import JSONResponse

# Modelos y servicios
from app.models.user_model import User
from app.services.accounts_service import AccountService

account_router = APIRouter()

@account_router.get("/account")
async def list_account(institution_name: str = Query(default=None, description="Nombre de la institucion para filtrar cuentas")):
    try:
        # Inicializar el servicio de cuentas
        account_service = AccountService()

        # Obtener la lista de cuentas según el filtro de institución
        print("institution_name")
        print(institution_name)
        if institution_name:
            account_list = account_service.list_account(institution_name)
        else:
            account_list = account_service.list_account()

        # Responder con la lista de cuentas
        return JSONResponse(content={"success": True, "data": account_list["results"]}, status_code=200)

    except Exception as ex:
        # Manejo de errores
        error_message = f"Error: {str(ex)}"
        return JSONResponse(content={"success": False, "message": error_message}, status_code=500)
