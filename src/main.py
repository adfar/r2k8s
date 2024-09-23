import httpx
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_index():
    return {"Hello": "World"}

@app.get("/api")
def read_api():
    r = httpx.get("https://api.stlouisfed.org/fred/releases/dates?api_key=45b25a0d9ecf2066830b75471a971dc9&file_type=json")
    return r.json()

@app.get("/api/v1/hello-world/")
def read_hello_world():
    """
    Return an API-like response.
    """
    return {"what": "road", "where": "kubernetes", "version": "v1"}
    