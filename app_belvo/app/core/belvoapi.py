import requests
from requests.auth import HTTPBasicAuth


def get_connection(endpoint):
    # URL de la API
    url = "https://sandbox.belvo.com/api/{endpoint}/"

    # Tus credenciales de autenticación
    username = "729e8ae4-efdd-4448-970b-1f423d356eeb"
    password = "ES_#Q*zXnid*28v-hEkp@AyEhPD5vDX_VT5oMM413sFf3M_AbACXbVoUnPb*rvU3"
