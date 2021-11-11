FROM python:3.9.7-slim-buster
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt install -y nodejs && \
    npm i -g npm
RUN pip3 install -U pip
COPY . /app
WORKDIR /app
RUN pip3 install --no-cache-dir -U -r requirements.txt
CMD [ "python3", "./main.py" ]
