import requests
from requests.auth import HTTPBasicAuth

from app.core.firebase import get_connection

class InstitutionService():
    

    def list_institutions(self):
        try:
            belvo_api_url = "https://sandbox.belvo.com/api"
            belvo_api_secret_id = "729e8ae4-efdd-4448-970b-1f423d356eeb"
            belvo_api_secret_password = "ES_#Q*zXnid*28v-hEkp@AyEhPD5vDX_VT5oMM413sFf3M_AbACXbVoUnPb*rvU3"
            # Obtener la conexión a Firebase
            response = requests.get(f"{belvo_api_url}/institutions", auth=HTTPBasicAuth(belvo_api_secret_id, belvo_api_secret_password))
            if response.status_code == 200:
                print("Solicitud exitosa!")
                # Para ver el contenido de la respuesta en formato JSON
                return response.json()
            else:
                print(f"Error en la solicitud. Código de estado: {response.status_code}")
        except Exception as ex:
            print(f"Error al traer lista: {ex}")
            return None