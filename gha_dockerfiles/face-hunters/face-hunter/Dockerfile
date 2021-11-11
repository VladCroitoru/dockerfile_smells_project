FROM python:3.8-slim

RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*
RUN pip install --upgrade pip

RUN cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python3 setup.py install --yes USE_AVX_INSTRUCTIONS

RUN apt-get install -y --fix-missing \
    libssl-dev \
    libffi-dev 
COPY . /root/FACE-HUNTER
RUN cd /root/FACE-HUNTER && \
    pip install -r requirements.txt
CMD export PYTHONPATH="${PYTHONPATH}:/root/FACE-HUNTER" && \
    cd /root/FACE-HUNTER && \
    python3 src/cli.py
