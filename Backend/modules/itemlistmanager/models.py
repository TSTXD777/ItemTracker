from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional, TypedDict
from marshmallow import Schema, fields
import marshmallow_dataclass as marshdata

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
    pass #TODO: Implementar la clase ItemList
    
    # Métodos para serialización y deserialización
    def to_typed_dict(self) -> "ItemListTypedDict":
        pass

    def to_schema(self):
        pass

    def from_schema(self, data):
        pass

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
    pass #TODO: Implementar la clase Tag

    # Métodos para serialización y deserialización
    def to_typed_dict(self) -> "ItemListTypedDict":
        pass

    def to_schema(self):
        pass

    def from_schema(self, data):
        pass

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
    pass #TODO: Implementar el TypedDict para ItemList

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
    pass #TODO: Implementar el TypedDict para Tag