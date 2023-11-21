from fastapi import FastAPI

app = FastAPI()

#hello
@app.get('/')
def hello_world():
    return "Hello world"