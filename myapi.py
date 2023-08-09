from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def new_function():
    return {"Hello": "World"}

@app.get("/about")
def about_function():
    return {'data': {'name':'anna'}}