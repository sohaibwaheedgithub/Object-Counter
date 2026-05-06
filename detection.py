# import supervision as sv
# from PIL import Image
# from ultralytics import YOLO
# import matplotlib.pyplot as plt

# model = YOLO('weights/best.pt')

# def detect_objects(image):

#     result = model.predict(image, verbose=False, conf=0.40)[0]
#     detections = sv.Detections.from_ultralytics(result)
    
#     n_cartons = 0
#     for conf in detections.confidence:
#         if conf >= 0.50:
#             n_cartons += 1
        
#     return n_cartons