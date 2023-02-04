import validaciones

def registrar_usuario(usuario:str, email:str) -> None:
    if validaciones.validar_email(email):
        print(f"{usuario} registrado con el correo {email} correctamente.")
    print ('El correo electronico no es valido')