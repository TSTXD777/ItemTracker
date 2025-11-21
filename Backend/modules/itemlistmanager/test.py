from pprint import pprint
from modules.itemlistmanager.apimodels import ItemListCreate
from modules.itemlistmanager.models import ItemList

object = ItemListCreate(
    name="Sample ItemList 2",
    description="This is a sample ItemList 2",
    tags_id=["tag1", "tag3"]
)


def main():
    # ItemList.create(object)
    #ItemList.query_all()
    
    print(ItemList.query_all())


if __name__ == "__main__":
    main()