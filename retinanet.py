#!/usr/bin/env python
# encoding: utf-8

import argparse
import time
import torch
import torchvision

parser = argparse.ArgumentParser()
parser.add_argument('--ipex', default=False, action="store_true")
args = parser.parse_args()

data = [torch.rand(3, 300, 400)]
net = torchvision.models.detection.retinanet_resnet50_fpn(pretrained=False)
net.eval()
if args.ipex:
    import intel_extension_for_pytorch as ipex
    net = net.to(memory_format=torch.channels_last)
    net = ipex.optimize(net)

with torch.no_grad():
    for _ in range(10):
        net(data)
    t0 = time.time()
    for _ in range(10):
        net(data)
    t1 = time.time()
    print('time: {:.5f} ms/f'.format((t1 - t0) / 10 * 1000))
