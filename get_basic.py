from ultralytics import YOLO
# TO get detect layer every basic module
yolo = YOLO("/home/jia/PycharmProjects/yolov10/runs/detect/basketball_yolov8s/weights/best.pt")
model = yolo.model
basic_layer = []
for name, module in model.model[-1].named_modules():
    if len(list(module.children())) == 0:
        basic_layer.append(name)
print(basic_layer)
