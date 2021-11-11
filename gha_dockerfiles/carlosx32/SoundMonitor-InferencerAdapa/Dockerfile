FROM ubuntu:bionic

RUN apt update &&\
    apt -y install libsndfile1 &&\
    apt install -y software-properties-common &&\
    apt install -y python3-pip &&\
    pip3 install https://download.pytorch.org/whl/cpu/torch-1.1.0-cp36-cp36m-linux_x86_64.whl &&\
    pip3 install https://download.pytorch.org/whl/cpu/torchvision-0.3.0-cp36-cp36m-linux_x86_64.whl

COPY requirements.txt /inferenciator/

RUN pip3 install -r /inferenciator/requirements.txt

COPY ./ /inferenciator/

WORKDIR /inferenciator/

CMD ["python3","inferencerStream.py"]
