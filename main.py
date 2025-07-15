from fastapi import FastAPI

app = FastAPI()

url_map= {}

@app.get("/")
async def say_hello():
    return "Hello"
