from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional, TypedDict
# from marshmallow import Schema, fields
import marshmallow_dataclass as marshdata
from pymongo import MongoClient
from pymongo.collection import Collection
import json

from .apimodels import ItemListCreate, ItemListEdit

db_client = MongoClient()
database = db_client["item_tracker_db"]

# Instrucciones
# 1 API -> 2 Función actual -> 3 Modifica la Base de Datos - 4 Retornar resultado


class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Status(Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    BLOCKED = "blocked"
    COMPLETED = "completed"

@dataclass
class ItemList(BaseModel):
    name: str
    id: Optional[str] # MongoDB genera un ID automáticamente
    description: Optional[str]
    date_created: datetime = Field(default_factory=datetime.now, exclude=True)
    date_modified: Optional[datetime] = Field(default=None, exclude=True)
    tags_id: List[str] # Contiene los IDs de las etiquetas asociadas al ítem

    # Métodos para serialización y deserialización
    def to_typed_dict() -> "ItemListTypedDict":
        return {
            "name": ItemList.name,
            #"id": ItemList.id,
            "description": ItemList.description,
            "date_created": ItemList.date_created.isoformat(),
            "date_modified": ItemList.date_modified.isoformat() if ItemList.date_modified else None,
            "tags_id": ItemList.tags_id
        }

    def to_schema(self):
        ItemListSchema = marshdata.class_schema(ItemList)
        schema = ItemListSchema()
        return schema.dump(self)

    def from_schema(self, data):
        ItemListSchema = marshdata.class_schema(ItemList)
        schema = ItemListSchema()
        return schema.load(data)

    
    # Métodos CRUD (Create, Read, Update, Delete)
    #TODO: Implementar la lógica de cada método

    def create(itemlist: ItemListCreate):
        
        ItemList.name = itemlist.name
        ItemList.description = itemlist.description
        ItemList.date_modified = None
        ItemList.date_created = datetime.now().isoformat()
        ItemList.tags_id = itemlist.tags_id

        try:
            itemlistcollection = database["itemlists"]
            result = itemlistcollection.insert_one(ItemList.to_typed_dict())
            print(f"Se creó el ItemList con ID: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            print(f"Error al crear el ItemList: {e}")
            return None

    def edit(item_id, new_data: ItemListEdit) -> dict:
        """
        Modifica un ItemList en la BD y retorna el resultado.
        
        Args:
            item_id: ObjectId del ItemList a editar
            new_data: Objeto ItemListEdit con los datos a actualizar
            
        Returns:
            dict: {"success": bool, "message": str, "data": dict or None}
        """
        try:
            itemlistcollection: Collection = database["itemlists"]
            
            # 1. Validar que el documento existe
            existing_item = itemlistcollection.find_one({"_id": item_id})
            if not existing_item:
                return {
                    "success": False,
                    "message": f"ItemList con ID {item_id} no encontrado.",
                    "data": None
                }
            
            # 2. Construir los datos a actualizar (solo los campos que se proporcionaron)
            update_data = new_data.model_dump(exclude_unset=True)
            
            # 3. Agregar fecha de modificación
            update_data["date_modified"] = datetime.now().isoformat()
            
            print(f"Datos a actualizar para ItemList con ID {item_id}: {update_data}")
            
            # 4. Ejecutar la actualización en la BD
            result = itemlistcollection.update_one(
                {"_id": item_id},
                {"$set": update_data}
            )
            
            # 5. Retornar resultado
            if result.matched_count == 0:
                return {
                    "success": False,
                    "message": f"No se encontró ningún ItemList con ID: {item_id}",
                    "data": None
                }
            elif result.modified_count >= 1:
                return {
                    "success": True,
                    "message": f"ItemList con ID {item_id} editado exitosamente.",
                    "data": update_data
                }
            else:
                return {
                    "success": True,
                    "message": f"ItemList con ID {item_id} encontrado pero no modificado (datos idénticos).",
                    "data": None
                }
                
        except Exception as e:
            print(f"Error al editar el ItemList: {e}")
            return {
                "success": False,
                "message": f"Error al editar el ItemList: {str(e)}",
                "data": None
            }
    def delete(): #TODO: Implementar la lógica de eliminación @mariozapata1408
        pass
    def query(): #TODO: Implementar la lógica de consulta @rchavez-code
        
        #buscar por un filtro proporcionado
        
        pass
    def query_by_id(self): #TODO: Implementar la lógica de consulta por ID @

        #buscar por el ID proporcionado

        pass
    def query_all():
        try:
            itemlistcollection = database["itemlists"]
            result = list(itemlistcollection.find())
            return result
        except Exception as e:
            print(f"Error al consultar los ItemLists: {e}")
            return None

@dataclass
class Item(BaseModel):
    name: str
    id: Optional[str] # MongoDB genera un ID automáticamente
    description: Optional[str]
    deadline: Optional[datetime]
    priority: Optional[Priority]
    status: Optional[Status]
    completed: Optional[bool]
    date_created: datetime
    date_completed: Optional[datetime]
    list_id: List[str] # Contiene los IDs de las listas a las que pertenece el ítem
    tags_id: List[str] # Contiene los IDs de las etiquetas asociadas al ítem


    # Métodos para serialización y deserialización
    def to_typed_dict(self) -> "ItemTypedDict":
        return {
            "name": self.name,
            "id": self.id,
            "description": self.description,
            "deadline": self.deadline.isoformat() if self.deadline else None,
            "priority": self.priority,
            "status": self.status,
            "completed": self.completed,
            "date_created": self.date_created.isoformat(),
            "date_completed": self.date_completed.isoformat() if self.date_completed else None,
            "list_id": self.list_id,
            "tags_id": self.tags_id
        }
    
    def to_schema(self):
        ItemSchema = marshdata.class_schema(Item)
        schema = ItemSchema()
        return schema.dump(self)
    
    def from_schema(self, data):
        ItemSchema = marshdata.class_schema(Item)
        schema = ItemSchema()
        return schema.load(data)

    # Métodos CRUD (Create, Read, Update, Delete)
    #TODO: Implementar la lógica de cada método

    def create(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass

    def query(self):
        pass

    def query_by_id(self):
        pass

    def query_all():
        pass

@dataclass
class Tag(BaseModel):
    name: str
    id: Optional[str] # MongoDB genera un ID automáticamente
    description: Optional[str]
    color: str

    # Métodos para serialización y deserialización
    def to_typed_dict(self) -> "TagTypedDict":
        return {
            "name": self.name,
            "id": self.id,
            "description": self.description,
            "color": self.color
        }

    def to_schema(self):
        TagSchema = marshdata.class_schema(Tag)
        schema = TagSchema()
        return schema.dump(self)

    def from_schema(self, data):
        TagSchema = marshdata.class_schema(Tag)
        schema = TagSchema()
        return schema.load(data)

    # Métodos CRUD (Create, Read, Update, Delete)
    #TODO: Implementar la lógica de cada método
    def create(self):
        pass
    def edit(self):
        pass
    def delete(self):
        pass
    def query(self):
        pass
    def query_by_id(self):
        pass
    def query_all():
        pass

class ItemListTypedDict(TypedDict):
    name: str
    id: Optional[str]
    description: Optional[str]
    date_created: str
    date_modified: Optional[str]
    tags_id: List[str]

class ItemTypedDict(TypedDict):
    name: str
    id: Optional[str]
    description: Optional[str]
    deadline: Optional[str]
    priority: Optional[Priority]
    status: Optional[Status]
    completed: Optional[bool]
    date_created: str
    date_completed: Optional[str]
    list_id: List[str]
    tags_id: List[str]

class TagTypedDict(TypedDict):
    name: str
    id: Optional[str]
    description: Optional[str]
    color: str