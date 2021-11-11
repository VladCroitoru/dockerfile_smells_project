FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get update && apt-get -y install --no-install-recommends apt-utils

RUN apt-get update && apt-get -y install python3.8 \
    python3-pip \
    python3-setuptools \
    ffmpeg \
    gnupg \
    && python3 -m pip install --upgrade pip \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get -y install wget
RUN wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add - && \
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" > /etc/apt/sources.list.d/mongodb-org-5.0.list && \
    apt-get -y update && \
    apt-get install -y mongodb-org



COPY . /app/api

WORKDIR /app/api

EXPOSE 5000

# RUN pip3 install torch==1.9.1+cpu torchvision==0.10.1+cpu torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html

RUN pip3 install --no-cache-dir -r requirements.txt

# VOLUME [ "/data/uploads", "/data/active_profile_audio", "/data/deleted_profile_audio" ]

ENV FLASK_APP=app.py

CMD python3 app.py
