FROM gtzago/nvidia-opencv
ARG PYTHON_VERSION=3.5
ARG NB_USER=ubuntu

USER root

RUN pip3 install tensorflow-gpu keras jupyter

USER $NB_USER    

EXPOSE 8888

CMD jupyter notebook --port=8888 --ip=0.0.0.0
