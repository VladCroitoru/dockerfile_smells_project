FROM tensorflow/tensorflow

RUN mkdir /home/fedexp
RUN python -m pip install --upgrade pip
RUN pip install pandas
RUN pip install sklearn
RUN pip install scikit-image
RUN pip install matplotlib
RUN pip install keras
RUN pip install torch
RUN pip install torchvision
RUN apt-get update && apt-get install -y wget unzip rsync
ENTRYPOINT /bin/bash
