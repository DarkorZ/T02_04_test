from fastapi import FastAPI
app = FastAPI(title="Sistema de Gestión de Minimercado API")
@app.get("/")
def read_root():
    return {"message": "API funcionando"}