from fastapi import APIRouter
from typing import Literal


router = APIRouter(prefix="", tags=["carton-counter"])


@router.get("/get-object-counts")
async def get_object_counts(object_to_count: str):
    if object_to_count.lower() != "carton":
        return {
            "success": False,
            "data": None,
            "message": f"{object_to_count} currently not Supported"
        }
    else:
        return {
            "success": True,
            "data": {
                "Object": object_to_count.title(),
                "Counts": 0
            },
            "message": None
        }