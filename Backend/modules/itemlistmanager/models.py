from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional, TypedDict
from marshmallow import Schema, fields
import marshmallow_dataclass as marshdata
from pymongo import MongoClient
from pymongo.collection import Collection

db_client = MongoClient()
database = db_client["item_tracker_db"]

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
class ItemList:
    name: str
    id: Optional[str] # MongoDB genera un ID automáticamente
    description: Optional[str]
    date_created: datetime
    date_modified: Optional[datetime]
    tags_id: List[str] # Contiene los IDs de las etiquetas asociadas al ítem

    # Métodos para serialización y deserialización
    def to_typed_dict(self) -> "ItemListTypedDict":
        return {
            "name": self.name,
            "id": self.id,
            "description": self.description,
            "date_created": self.date_created.isoformat(),
            "date_modified": self.date_modified.isoformat() if self.date_modified else None,
            "tags_id": self.tags_id
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
    def create(self):
        self.itemlist_collection = database["itemlists"]
        try:
            result = self.itemlist_collection.insert_one(self.to_typed_dict())
            print(f"Se creó el ItemList con ID: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            print(f"Error al crear el ItemList: {e}")
            return None
    
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
class Item:
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
class Tag:
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