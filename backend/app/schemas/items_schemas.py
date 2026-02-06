from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    order_id: int
    restaurant_id: int
    food_item: str
    order_time: str
    delivery_time: str
    delivery_distance: float
    order_value: float
    delivery_method: str
    traffic_condition: str
    weather_condition: str
