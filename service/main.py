from fastapi import FastAPI

app = FastAPI(title="Molecule Solubility Service")


@app.get("/")
def get_message():
    return {"message": "hello..."}

@app.post("/train")
def get_message():
    return {"message": "training model"}

@app.post("/predict")
def get_message():
    return {"message": "making inference"}
