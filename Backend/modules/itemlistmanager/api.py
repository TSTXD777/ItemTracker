from fastapi import FastAPI
# Use explicit relative import so the module can be imported from the package/root reliably
from .models import ItemList
from .apimodels import ItemListCreate

app = FastAPI()
# Comando para ejecutar el servidor FastAPI:
# fastapi dev modules/itemlistmanager/api.py --port 8564
# uvicorn modules.itemlistmanager.api:app --reload --port 8564


# Crear función de API @app.tipo
# Añadir la función def nombre_función(parámetros):
# añadir un try-except para manejar errores 

@app.post("/itemlistmanager/itemlists/create/", tags=["ItemList"])
def create_itemlist(inputdata: ItemListCreate):
    try:
        ItemList.create(inputdata)
        return {"message": "ItemList creado con éxito."}
    except Exception as e:
        return {"message": f"Error al crear el ItemList: {str(e)}"}
    
@app.get("/itemlistmanager/itemlists/get_all/", tags=["ItemList"])
def get_all_itemlists():
    try:
        items = ItemList.query_all()

        for item in items:
            item["_id"] = str(item["_id"])  # Convertir ObjectId a string

        return {
            "query": items,
            "message": "Consulta de ItemLists exitosa."        
            }
    except Exception as e:
        return {"message": f"Error al consultar los ItemLists: {str(e)}"}



@app.post("/itemlistmanager/itemlists/edit/", tags=["ItemList"])
def edit_itemlist(inputdata):
    try:
        #TODO: Implementar la lógica de edición @eder2511
        pass  
    except Exception as e:
        return {"message": f"Error al editar el ItemList: {str(e)}"}