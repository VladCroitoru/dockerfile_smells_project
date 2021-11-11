FROM ubuntu:latest

WORKDIR /usr/src/app

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt -y install ffmpeg \
    && apt install -y software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt update \
    && apt install -y python3-pip \
    && python3 -m pip install -U pip \
    && pip install --upgrade pip \
    && apt install -y curl\
    && curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh\
    && bash nodesource_setup.sh\
    && apt install -y nodejs\
    && apt install -y ffmpeg


COPY . alfred/
RUN python3 -m pip install --no-cache-dir -r alfred/python/requirements.txt \ 
    && npm install alfred/src/

CMD ["bash", "alfred/alfred.sh"]