FROM continuumio/anaconda3:5.1.0

MAINTAINER Eric Hans

ENV PYTHONPATH /opt/conda/lib/python3.6/site-packages/rle_python_interface:/gym-rle

RUN conda install numpy pandas scipy scikit-learn tensorflow theano keras -y && \
    conda install pytorch torchvision pytorch-cpu torchvision -c pytorch -y

RUN git clone https://github.com/erichans/Retro-Learning-Environment.git && git clone https://github.com/erichans/gym-rle.git

RUN apt-get update && apt-get install libsdl1.2-dev libsdl-gfx1.2-dev libsdl-image1.2-dev cmake g++ alsa-base alsa-utils pulseaudio x11vnc xvfb -y

WORKDIR /Retro-Learning-Environment
RUN pip install .

WORKDIR /gym-rle
RUN pip install .

RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers && \
    chmod 0440 /etc/sudoers && \
    chown ${uid}:${gid} -R /home/developer

WORKDIR /openai
ENTRYPOINT python agent-openai.py

USER developer
ENV HOME /home/developer

