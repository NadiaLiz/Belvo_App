# app/services/user_service.py

from app.core.firebase import get_connection
from app.models.user_model import User
from fastapi import FastAPI, HTTPException, status

from fastapi.responses import JSONResponse
import uuid

#db = initialize_firebase()

class UserService:
    @staticmethod
    async def authenticate_user(username: str, password: str):
        try:
            connection = get_connection()
            auth = connection.auth()
            user_return = auth.sign_in_with_email_and_password(username, password)
            encoded_token = user_return["idToken"]
            return {'success': True, 'token': f"Bearer {encoded_token}"}
            #return user_return
        except Exception as ex:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"message": "ERROR", "success": False}
            )
        
    @staticmethod
    def create_user(user: User):
        print("Creando usuario service 001")
        try:
            print("Creando usuario service 002")
            # Obtener la conexión a Firebase
            connection = get_connection()
            # Crear un nuevo usuario en Firebase Authentication
            auth = connection.auth()
            new_user = auth.create_user_with_email_and_password(
                user.email, user.password)
            return new_user
        except Exception as ex:
            print(f"Error al crear usuario: {ex}")
            return "Error al crear usuario"
    
    @staticmethod
    async def get_user_by_username(id_token: str):
        try:
            connection = get_connection()
        
            print("connection  @.@")
            print(connection)
            # Crear un nuevo usuario en Firebase Authentication
            auth = connection.auth()
            print("auth  @.@")
            print(auth)
            decoded_token  = auth.get_account_info(id_token)
            
            #print("decoded_token  @.@")
            #print(decoded_token)
            return decoded_token['User']
            #return "Error al crear usuario"
        except Exception as ex:
            print(f"Error al crear usuario: {ex}")
            return None