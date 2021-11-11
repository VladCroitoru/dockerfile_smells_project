# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# start from the jupyter image with R, Python, and Scala (Apache Toree) kernels pre-installed
FROM jupyter/minimal-notebook

# install the kernel gateway
RUN pip install jupyter_kernel_gateway

# run kernel gateway on container start, not notebook server
EXPOSE 8888
CMD ["jupyter", "kernelgateway", "--KernelGatewayApp.ip=0.0.0.0", "--KernelGatewayApp.port=8888"]
