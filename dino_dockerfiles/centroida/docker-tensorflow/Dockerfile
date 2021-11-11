# An image with Keras and Hyperas build on top of Tensorflow.

FROM tensorflow/tensorflow:1.6.0-gpu-py3

LABEL maintainer="Centroida [https://centroida.ai] <info@centroida.ai>"

# Install Keras and Hyperas
RUN apt-get update -y \
	&& apt-get install vim -y \
	&& pip3 install hyperas \
	&& pip3 install networkx==1.11 \
	&& apt-get install libhdf5-serial-dev -y

# TensorBoard
EXPOSE 6006

# Jupyter
EXPOSE 8888
