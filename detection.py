# import colorsys
# import supervision as sv
# from PIL import Image
# from ultralytics import YOLO
# import matplotlib.pyplot as plt
# import supervision as sv
# from PIL import Image



# def annotate(image: Image.Image, detections: sv.Detections) -> Image.Image:
#     class_names = detections.data.get("class_name")
#     labels = []

#     for index in range(len(detections)):
#         class_name = class_names[index] if class_names is not None else "Box"
#         labels.append(f"{index + 1} {class_name}")

#     color_count = max(len(detections), 1)
#     colors = []

#     for index in range(color_count):
#         hue = (index * 0.618033988749895) % 1
#         red, green, blue = colorsys.hsv_to_rgb(hue, 0.65, 1.0)
#         colors.append(
#             f"#{int(red * 255):02x}{int(green * 255):02x}{int(blue * 255):02x}"
#         )

#     color = sv.ColorPalette.from_hex(colors)

#     text_scale = sv.calculate_optimal_text_scale(resolution_wh=image.size)

#     box_annotator = sv.BoxAnnotator(
#         color=color,
#         color_lookup=sv.ColorLookup.INDEX
#     )
#     label_annotator = sv.LabelAnnotator(
#         color=color,
#         text_color=sv.Color.BLACK,
#         text_scale=text_scale,
#         color_lookup=sv.ColorLookup.INDEX,
#         smart_position=True
#     )

#     out = image.copy()
#     out = box_annotator.annotate(out, detections)
#     out = label_annotator.annotate(out, detections, labels=labels)
#     out.thumbnail((1000, 1000))
#     return out



# model = YOLO('new_weights/best.pt')
# #model = YOLO('weights/last.pt')

# def detect_objects(image):

#     result = model.predict(image, verbose=False, conf=0.50)[0]
#     detections = sv.Detections.from_ultralytics(result)
#     detections = detections.with_nms(threshold=0.50, class_agnostic=True)
#     ann_img = annotate(image, detections)
        
#     return len(detections), ann_img


# l, i = detect_objects(Image.open(r"C:\Users\EXPK0322\OneDrive - Pakistan Oxygen Limited\Carton Images\Container Carton Pics\1772077019250.jpg"))
# print("No of cartons: ", l)
# i.show()


