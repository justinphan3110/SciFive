import os


"""Note: Install JAX tutorial here"""
"""https://github.com/google/jax#pip-installation-gpu-cuda"""
"""CUDA"""
"""pip install jaxlib==0.4.1+cuda11.cudnn86 -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html"""

"""Install T5X."""
os.system("pip install git+https://github.com/google-research/t5x -f https://storage.googleapis.com/jax-releases/libtpu_releases.html")

"""Install Extra Requirements"""
# nest-asyncio is for colab notebook running

os.system("pip install t5 seqeval datasets gsutil==5.8 tensorflow_datasets==4.8.1 lxml==4.9.2 nest-asyncio==1.5.6")
