# retinanet_ipex

## Getting started
Follow instructions at [Installation Guide](https://intel.github.io/intel-extension-for-pytorch/tutorials/installation.html) to install PyTorch and Intel(R) Extension for PyTorch.
```bash
python -m pip install mkl numpy
python retinanet.py
python retinanet.py --ipex
python -m intel_extension_for_pytorch.cpu.launch --ninstance 1 --node_id 0 retinanet.py
python -m intel_extension_for_pytorch.cpu.launch --ninstance 1 --node_id 0 retinanet.py --ipex
```
