#coding=utf-8
import torch
import torch.nn as nn
import torch.nn.functional as F

# 定义一个简单的模型
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 20, 5)
        self.conv2 = nn.Conv2d(20, 64, 5)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        return x

# 实例化模型
model = SimpleModel()

# 定义一个钩子函数，用于记录输出
def forward_hook(module, input, output):
    print(f"Forward hook called on {module}")
    print(f"Input: {input}")
    print(f"Output: {output}")

# 注册前向钩子
hooks = []
for layer in model.children():
    hooks.append(layer.register_forward_hook(forward_hook))

# 创建一些输入数据
input_data = torch.randn(1, 1, 32, 32)

# 前向传播
output = model(input_data)

# 移除钩子
for hook in hooks:
    hook.remove()

