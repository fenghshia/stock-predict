### Windows 11 Nvdia GPU

1. Install MSVC 2019
2. Install [CUDA 11.2](https://developer.download.nvidia.com/compute/cuda/11.2.2/local_installers/cuda_11.2.2_461.33_win10.exe)
3. Install [cuDNN 8.1](https://developer.nvidia.com/compute/machine-learning/cudnn/secure/8.1.1.33/11.2_20210301/cudnn-11.2-windows-x64-v8.1.1.33.zip)
4. Install [Conda](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)

Caution! Tensorflow gpu support only befor v2.11 on windows. In this project use tensorflow 2.10. Watch [here](https://www.tensorflow.org/install/source_windows#gpu) for more detail.

```powershell
conda create -n sp python=3.10
conda activate sp
python -m pip install -U "tensorflow<2.11" akshare scikit-learn pandas tqdm matplotlib jupyter notebook prettytable import-ipynb
```

### MacOS GPU support

```powershell
conda create -n sp
conda activate sp
python -m pip install -U tensorflow tensorflow-metal akshare scikit-learn matplotlib jupyter notebook prettytable import-ipynb
```

- [Miniconda Document](https://docs.anaconda.com/miniconda/install/)

- [CUDA archive](https://developer.nvidia.com/cuda-toolkit-archive)

- [cuDNN archive](https://developer.nvidia.com/rdp/cudnn-archive)

- [MacOS GPU Support](https://developer.apple.com/metal/tensorflow-plugin/)

### Jetson Nano with Jetpack 4.6.6

1. Install CUDA

```powershell
sudo apt -y install cuda-toolkit-10-2
```

2. Install cuDNN

```powershell
sudo apt -y install nvidia-cudnn8
```

3. Install TensorRT

```powershell
sudo apt -y install nvidia-tensorrt
```

4. Install conda-forge and config

```powershell
zsh -c "$(curl https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh)"
conda create -n ai-env python=3.6
conda activate ai-env
conda install h5py==3.1.0
wget -P ~/Download https://developer.download.nvidia.com/compute/redist/jp/v461/pytorch/torch-1.11.0a0+17540c5+nv22.01-cp36-cp36m-linux_aarch64.whl
python -m pip install ~/Download/torch-1.11.0a0+17540c5+nv22.01-cp36-cp36m-linux_aarch64.whl
```



### Dev Document

- [Akshare Document](https://akshare.akfamily.xyz/)
