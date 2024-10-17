Instrucciones para inySQL.py:
Modificar (línea 4) target_url = "http://10.0.2.15:8080/AltoroJ/doLogin" con la IP donde esté publicado la app de Altoro.
Modificar (línea 8) headers con el contenido del http request de un login bien formado enviado la target url. Esto se puede realizar con Burp o ZAP.

Instrucciones para XSS.py:
Modificar (línea 4) base_url = "http://10.0.2.15:8080/AltoroJ/search.jsp" con la IP donde esté publicado la app de Altoro.
