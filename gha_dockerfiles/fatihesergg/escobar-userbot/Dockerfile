FROM python:3.9.7-slim-buster

WORKDIR /EscobarBot/

RUN apt-get -y update && \
    apt-get install -y \
    ffmpeg \
    python3-pip \
    git \
    wget \
    tar

RUN apt-get install python3-dev python3-pip libpq5 libjpeg-dev tesseract-ocr libpoppler-cpp-dev imagemagick virtualenv libopencv-dev zbar-tools libzbar0 libzbar-dev libfuzzy-dev build-essential -y

RUN git clone https://github.com/fatihesergg/escobar-userbot /EscobarBot/

RUN pip install -r requirements.txt

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz && \
    tar -xvzf geckodriver*  && \
    chmod +x geckodriver 
    
CMD ['python3','start.py']
    
