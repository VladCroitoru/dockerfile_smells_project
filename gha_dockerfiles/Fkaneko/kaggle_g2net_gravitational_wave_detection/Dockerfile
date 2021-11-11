From nvcr.io/nvidia/pytorch:21.08-py3 
Copy install.sh /src/python/

RUN pip install --upgrade pip & sh /src/python/install.sh
ENV DIR="/workspace/kaggle/g2net_gravitational_wave_detection/"
RUN mkdir -p $DIR
WORKDIR $DIR
