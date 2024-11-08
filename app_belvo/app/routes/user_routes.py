from fastapi import APIRouter, HTTPException
from app.services.user_service import UserService
from app.models.user_model import User, UserLogin


router = APIRouter()


@router.post("/login")
async def login(request: UserLogin):
    print("Prueba")
    return await UserService.authenticate_user(request.email, request.password)


@router.post("/signup")
async def signup(user: User):
    print("saludos @.@")
    existing_user = await UserService.get_user_by_username(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="email already exists")
    
    return UserService.create_user(user)


@router.get("/profile")
async def get_user():
    print("request")
    try:
        #if authorization is None:
        #    raise HTTPException(
        #        status_code=401, 
        #        detail="Token no proporcionado en el encabezado Authorization"
        #    )
        #scheme, token = authorization.split()
        response = {
        
                        "createdAt": "1726678088464",
                        "email": "prueba@gmail.com",
                        "emailVerified": False,
                        "lastLoginAt": "1731033009679",
                        "lastRefreshAt": "2024-11-08T02:30:09.679Z",
                        "localId": "UChrkBxGlzVi7uq4qfVwzPdzpvW2",
                        "passwordHash": "UkVEQUNURUQ=",
                        "passwordUpdatedAt": 1726678088464,
                        "providerUserInfo": [
                            {
                                "email": "prueba@gmail.com",
                                "federatedId": "prueba@gmail.com",
                                "providerId": "password",
                                "rawId": "prueba@gmail.com"
                            }
                        ],
                        "validSince": "1726678088"
            }
        if response:
            return {'success': True, 'user': response}
        else:
            return {'success': False, 'message': 'Failed to retrieve profile'}, 400

    except Exception as ex:
        # Manejo de errores
        return {'success': False, 'message': f"Error: {str(ex)}"}, 500
