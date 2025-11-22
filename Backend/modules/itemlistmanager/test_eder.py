from modules.itemlistmanager.apimodels import ItemListEdit
from modules.itemlistmanager.models import ItemList

object = ItemListEdit(
  id = "string4",
  name = "string4",
  description = "string4",
  tags_id= [
    "string4"
  ]
)

def main():
    ItemList.edit(object)
    
if __name__ == "__main__":
    main()