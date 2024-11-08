import requests
from requests.auth import HTTPBasicAuth

from app.core.firebase import get_connection


class AccountService():

    def list_account(self, institution_name= None):
        try:
            belvo_api_url = "https://sandbox.belvo.com/api"
            belvo_api_secret_id = "5b445697-0d9a-45c0-b037-0bd73e9d48f5"
            belvo_api_secret_password = "bOyR8ir3HfGsg-kfhXXo6GnFhb78r#PMNilbyQPDozMOs8h_UdgzO9yWmhDhwtS@"
            # Obtener la conexión a Firebase
            #print(f"{belvo_api_url}/accounts?institution__in={institution_name}")
            if institution_name:
                response = requests.get(f"{belvo_api_url}/accounts?link__in=dafdee05-56ff-462d-9abb-07d44ce7fe32&institution__in={institution_name}", auth=HTTPBasicAuth(belvo_api_secret_id, belvo_api_secret_password))
            else:
                response = requests.get(f"{belvo_api_url}/accounts", auth=HTTPBasicAuth(belvo_api_secret_id, belvo_api_secret_password))
                
            if response.status_code == 200:
                print("Solicitud exitosa!")
                # Para ver el contenido de la respuesta en formato JSON
                return response.json()
            else:
                print(f"Error en la solicitud. Código de estado: {response.status_code}")
        except Exception as ex:
            print(f"Error al traer lista: {ex}")
            return None