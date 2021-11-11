FROM nvidia/cuda:8.0-cudnn6-runtime-ubuntu16.04
RUN apt-get update && apt-get install -y python3 python3-pip git-core
RUN git clone https://github.com/keithito/tacotron
RUN git clone https://github.com/ArkaneCow/tacotron-models
WORKDIR /tacotron
RUN git reset --hard 8edcd55b3f08f0492340e8b3ee60a693138f5473
RUN pip3 install -r requirements.txt
RUN pip3 install tensorflow-gpu==1.3
CMD python3 /tacotron/demo_server.py --checkpoint /tacotron-models/mxgray_nancy/model.ckpt-250000