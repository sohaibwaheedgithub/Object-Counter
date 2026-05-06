from fastapi import APIRouter
from typing import Literal
#import supervision as sv
import base64
from io import BytesIO
#from PIL import Image
from typing import TypedDict
#from detection import detect_objects

router = APIRouter(prefix="", tags=["carton-counter"])




class RequestBody(TypedDict):
    object_to_count: str
    image_base64: str = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMAASsJTYQAAAAASUVORK5CYII="


@router.post("/get-object-counts")
async def get_object_counts(payload: RequestBody):
    if payload["object_to_count"].lower() != "carton":
        return {
            "header": {
                "success": False,
                "data": None,
                "message": f"{payload["object_to_count"]} currently not Supported"
            }
        }
    else:

        # img = Image.open("images/3629_13.jpg")

        # buffer = BytesIO()
        # img.save(buffer, format="PNG")

        # image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        
        
        #image = Image.open(BytesIO(base64.b64decode(payload["image_base64"])))
        
        #n_cartons = detect_objects(image)

        return {
            "header": {
                "success": True,
                "data": {
                    "Object": payload["object_to_count"].title(),
                    "Counts": 0
                },
                "message": None
            }
        }