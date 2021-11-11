FROM ubuntu:21.10
ENV DEBIAN_FRONTEND=noninteractive
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ impish universe" > /etc/apt/sources.list.d/docker.list && \
    apt update && \
    apt install -y apt-utils
RUN apt install -y --no-install-recommends \
    aria2 \
    curl \
    git \
    g++ \
    build-essential \
    gnupg2 \
    ffmpeg \
    figlet \
    jq \
    libpq-dev \
    libevent-dev \
    neofetch \
    netbase \
    wget \
    unzip \
    xz-utils \
    python3-pip \
    python3-psycopg2
RUN pip3 install --upgrade pip
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb
RUN wget -qP /tmp/ "https://chromedriver.storage.googleapis.com/94.0.4606.41/chromedriver_linux64.zip" && \
    unzip -o /tmp/chromedriver_linux64.zip -d /usr/bin && \
    chmod 755 /usr/bin/chromedriver
RUN curl https://raw.githubusercontent.com/dunggvn/Forkzilion/Stuff/requirements.txt -o requirements.txt && \
    pip3 install --no-cache-dir -r requirements.txt && \
    rm requirements.txt
