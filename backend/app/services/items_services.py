from app.repositories.items_repo import load_all, save_all
from app.schemas.items_schemas import Item
from fastapi import HTTPException

def list_items():
    return load_all()

def create_item(payload: Item):
    items = load_all()
    new_item = payload.dict()
    items.append(new_item)
    save_all(items)
    return new_item

def get_item_by_id(item_id: int):
    items = load_all()
    for item in items:
        if item['order_id'] == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")

def update_item(item_id: int, payload: Item):
    items = load_all()
    for idx, item in enumerate(items):
        if item['order_id'] == item_id:
            items[idx].update(payload.dict())
            save_all(items)
            return items[idx]
    raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")

def delete_item(item_id: int):
    items = load_all()
    items = [item for item in items if item['order_id'] != item_id]
    save_all(items)
