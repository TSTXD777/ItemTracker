from dataclasses import dataclass
from typing import List, Optional
from pydantic import BaseModel


class ItemListCreate(BaseModel):
    name: str
    description: Optional[str]
    tags_id: List[str]  # Contiene los IDs de las etiquetas asociadas al ítem