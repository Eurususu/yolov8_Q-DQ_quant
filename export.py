#coding=utf-8
from ultralytics import YOLO
from pytorch_quantization import nn as quant_nn
from pytorch_quantization import quant_modules
quant_modules.initialize()
quant_nn.TensorQuantizer.use_fb_fake_quant = True
model = YOLO("/home/jia/PycharmProjects/yolov8-pytorch_quantization/weights/yolov8s-max-1024_relu_basketball.pt")
model.fuse()
model.info(verbose=False)  # Print model information
model.export(format='onnx',imgsz=(736, 2560), opset=13, dynamic=True, simplify=True)
quant_nn.TensorQuantizer.use_fb_fake_quant = False
model.export = False
