from fastapi import FastAPI
# Use explicit relative import so the module can be imported from the package/root reliably
from .models import ItemList

app = FastAPI() #uvicorn api:app --reload --port 8564

@app.post("/itemlistmanager/itemlists/create/", tags=["ItemList"])
def create_itemlist(itemlist: ItemList):
    try:
        itemlist.create()
        return {"message": "ItemList creado con éxito."}
    except Exception as e:
        return {"message": f"Error al crear el ItemList: {str(e)}"}
