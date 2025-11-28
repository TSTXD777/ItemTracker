from bson import ObjectId
from fastapi import FastAPI
# Use explicit relative import so the module can be imported from the package/root reliably
from .models import ItemList
from .apimodels import ItemListCreate, ItemListEdit

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
def edit_itemlist(inputdata: ItemListEdit):
    try:
         # 1. Validar que el ID no esté vacío
        if not inputdata.id:
            raise ValueError("El ID del ItemList no puede estar vacío.")
        
        # 2. Convertir el ID a ObjectId si es necesario
        try:
            item_id = ObjectId(inputdata.id)
        except Exception:
            raise ValueError(f"ID inválido: {inputdata.id}")
        
        # 3. Llamar a la función interna que modifica la BD y retorna resultado
        result = ItemList.edit(item_id, inputdata)
        
        # 4. Retornar el resultado a la API
        return result
        
    except ValueError as ve:
        return {"success": False, "message": f"Error de validación: {str(ve)}", "data": None}
    except Exception as e:
        return {"success": False, "message": f"Error al editar el ItemList: {str(e)}", "data": None}