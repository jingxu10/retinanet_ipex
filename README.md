# retinanet_ipex

## Getting started
```bash
python -m pip install torch==1.10.0+cpu torchvision==0.11.1+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
python -m pip install intel_extension_for_pytorch==1.10.0 -f https://software.intel.com/ipex-whl-stable
python -m pip install psutil mkl numpy
python retinanet.py
python retinanet.py --ipex
python -m intel_extension_for_pytorch.cpu.launch --ninstance 1 --socket 0 retinanet.py
python -m intel_extension_for_pytorch.cpu.launch --ninstance 1 --socket 0 retinanet.py --ipex
```
