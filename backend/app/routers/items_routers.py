from fastapi import APIRouter, HTTPException
from app.schemas.items_schemas import Item
from app.services.items_service import list_items, create_item, get_item_by_id, update_item, delete_item

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/", response_model=List[Item])
def get_items():
    return list_items()

@router.post("/", response_model=Item, status_code=201)
def post_item(payload: Item):
    return create_item(payload)

@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int):
    return get_item_by_id(item_id)

@router.put("/{item_id}", response_model=Item)
def put_item(item_id: int, payload: Item):
    return update_item(item_id, payload)

@router.delete("/{item_id}", status_code=204)
def remove_item(item_id: int):
    delete_item(item_id)
    return None
