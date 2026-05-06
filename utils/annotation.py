# import supervision as sv
# from PIL import Image

# def annotate(image: Image.Image, detections: sv.Detections) -> Image.Image:
#     color = sv.ColorPalette.from_hex([
#         "#9999ff", "#3399ff", "#66ffff", "#33ff99", "#66ff66", "#99ff00",
#         "#ffff00", "#ff9b00", "#ff8080", "#ff66b2", "#ff66ff", "#b266ff",
#     ])

#     text_scale = sv.calculate_optimal_text_scale(resolution_wh=image.size)

#     box_annotator = sv.BoxAnnotator(color=color)
#     label_annotator = sv.LabelAnnotator(
#         color=color,
#         text_color=sv.Color.BLACK,
#         text_scale=text_scale,
#         smart_position=True
#     )

#     out = image.copy()
#     out = box_annotator.annotate(out, detections)
#     out = label_annotator.annotate(out, detections)
#     out.thumbnail((1000, 1000))
#     return out
