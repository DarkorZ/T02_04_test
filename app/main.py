from fastapi import FastAPI
from app.controllers import inventory_controller

app = FastAPI(
    title="Sistema de Gestión de Minimercado API",
    description="Backend para la gestión de inventario, ventas y caja [cite: 49]",
    version="1.0.0"
)

# Incluir los controladores 
app.include_router(inventory_controller.router)

@app.get("/")
def read_root():
    return {"message": "API de Minimercado funcionando correctamente"}