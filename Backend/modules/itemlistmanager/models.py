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

from .apimodels import ItemListCreate

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
        ItemList.date_created = datetime.now()
        ItemList.tags_id = itemlist.tags_id

        try:
            itemlistcollection = database["itemlists"]
            result = itemlistcollection.insert_one(ItemList.to_typed_dict())
            print(f"Se creó el ItemList con ID: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            print(f"Error al crear el ItemList: {e}")
            return None

    def edit(): #TODO: Implementar la lógica de edición @eder2511
        try:
            return str("funciona")
        except Exception as e:
            print(f"Error al editar el ItemList: {e}")
            return None
        #editar en la base de datos según los parámetros especificados

        #actualizar la fecha de modificación

        pass
    def delete(self): #TODO: Implementar la lógica de eliminación @eder2511
        pass
    def query(self): #TODO: Implementar la lógica de consulta
        pass
    def query_by_id(self): #TODO: Implementar la lógica de consulta por ID
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