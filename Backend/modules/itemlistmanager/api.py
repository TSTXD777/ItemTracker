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
        # 1. Obtener el ID del objeto a editar
        item_id = inputdata.id
        
        # 2. Preparar los nuevos datos para la función edit
        # Usamos el objeto ItemListEdit completo ya que la función ItemList.edit 
        # acepta un objeto de modelo que contiene los campos a actualizar.
        # Si ItemList.edit requiere solo los campos de ItemListCreate, 
        # podría ser necesario remapear o usar directamente ItemListEdit
        
        # 3. Llamar a la función estática ItemList.edit()
        # Nota: La función ItemList.edit requiere el ID y los new_data.
        success = ItemList.edit(item_id, inputdata)

        if success:
            return {"message": f"ItemList con ID {item_id} editado con éxito."}
        else:
            # Si la función edit retorna False (ej: no se encontró el ID)
            return {"message": f"Error: No se pudo encontrar o editar el ItemList con ID {item_id}."}  
    except Exception as e:
        return {"message": f"Error al editar el ItemList: {str(e)}"}