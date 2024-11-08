from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import JSONResponse

# Modelos y servicios
from app.models.user_model import User
from app.services.transactions_service import TransactionService

transaction_router = APIRouter()

@transaction_router.get("/transactions")
async def list_transactions(account_id: str = Query(default=None, description="ID de la cuenta para filtrar transacciones")):
    try:
        # Inicializar el servicio de transacciones
        transaction_service = TransactionService()

        # Obtener la lista de transacciones y calcular el balance si se pasa un account_id
        if account_id:
            transactions_list = transaction_service.list_transactions(account_id)
            balance = transaction_service.info_balance(transactions_list)
        else:
            transactions_list = transaction_service.list_transactions()
            balance = None

        # Responder con la lista de transacciones y el balance (si aplica)
        return JSONResponse(content={"success": True, "data": transactions_list["results"], "balance": balance}, status_code=200)

    except Exception as ex:
        # Manejo de errores
        error_message = f"Error: {str(ex)}"
        return JSONResponse(content={"success": False, "message": error_message}, status_code=500)
