from dataclasses import dataclass
from typing import List, Optional
from pydantic import BaseModel


class ItemListCreate(BaseModel):
    name: str
    description: Optional[str]
    tags_id: List[str]  # Contiene los IDs de las etiquetas asociadas al ítem

class ItemListEdit(BaseModel):
    id: str  # ID del ItemList a editar
    name: Optional[str]
    description: Optional[str]
    tags_id: Optional[List[str]]  # Contiene los IDs de las etiquetas asociadas al ítem