# retinanet_ipex

## Getting started
```bash
python -m pip install torch==1.10.0+cpu torchvision==0.11.1+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
wget https://github.com/jingxu10/retinanet_ipex/releases/download/v1.10/intel_extension_for_pytorch-1.10.0+cpu-cp38-cp38-linux_x86_64.whl
python -m pip install intel_extension_for_pytorch-1.10.0+cpu-cp38-cp38-linux_x86_64.whl
python -m pip install psutil mkl numpy
python retinanet.py
python retinanet.py --ipex
python -m intel_extension_for_pytorch.cpu.launch --ninstance 1 --socket 0 retinanet.py
python -m intel_extension_for_pytorch.cpu.launch --ninstance 1 --socket 0 retinanet.py --ipex
```
