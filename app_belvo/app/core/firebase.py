import pyrebase


def get_connection():
    print("Coneccion DB")
    try:
        config = {
            "apiKey": "AIzaSyBOk3MkuL2DY_XZ0rBi7uFPC6q6fgmSR3U",
            "authDomain": "belvo-app.firebaseapp.com",
            "projectId": "belvo-app",
            "storageBucket": "belvo-app.appspot.com",
            "messagingSenderId": "240980248638",
            "appId": "1:240980248638:web:61fdab33dc5bd0e5aee96f",
            "databaseURL": ""
        }

        return pyrebase.initialize_app(config)

    except Exception as ex:
        print(f"Ocurrió un error en la coneccion a firebase: {ex}")
