import requests
import sys
# Definimos la URL del sitio vulnerable
base_url = "http://10.0.2.15:8080/AltoroJ/search.jsp"
# Datos para probar la vulnerabilidad XSS
xss_payload = "<script>alert('Vulnerabilidad XSS Expuesta!')</script>"
# Parámetros de búsqueda con el payload XSS
params = {
    "query": xss_payload
}
# Realizamos la petición GET para comprobar la vulnerabilidad XSS
try:
    response = requests.get(base_url, params=params)
    # Verificamos si el payload XSS aparece en la respuesta
    if xss_payload in response.text:
        print("La aplicación es vulnerable a XSS. Se detectó la ejecución del payload en la respuesta.")
        sys.exit(1)
    else:
        print("No se detectó la vulnerabilidad XSS. Es posible que el sitio tenga protecciones.")
        sys.exit(0)
except requests.exceptions.RequestException as e:
    print(f"Error al conectarse al sitio: {e}")
    sys.exit(0)