from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

# Modelos y servicios
from app.models.user_model import User
from app.services.institutions_service import InstitutionService

# Crear un router para las rutas de bancos
institucion_router = APIRouter()

@institucion_router.get("/institutions")
async def list_institutions():
    try:
        # Inicializar el servicio de bancos
        institutionsService = InstitutionService()
        print("Creando institutions router")
        
        # Obtener la lista de bancos
        institucions_list = institutionsService.list_institutions()

        # Responder con la lista de bancos
        return JSONResponse(content={"success": True, "data": institucions_list["results"]}, status_code=200)

    except Exception as ex:
        # Manejo de errores
        error_message = f"Error: {str(ex)}"
        return JSONResponse(content={"success": False, "message": error_message}, status_code=500)
