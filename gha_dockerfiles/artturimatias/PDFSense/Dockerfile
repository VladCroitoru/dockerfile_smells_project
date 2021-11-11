FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y curl poppler-utils graphicsmagick imagemagick poppler-data vim tesseract-ocr python3-pip img2pdf tesseract-ocr-fin tesseract-ocr-swe

# Install Node.js
RUN apt-get install --yes curl
RUN curl --silent --location https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs


COPY package.json /src/package.json
RUN cd /src; npm install

RUN useradd -rm -d /home/node -s /bin/bash  -u 1000 node
COPY noteshrink/requirements.txt /home/node/requirements.txt
RUN cd /home/node; pip3 install -r requirements.txt -t .

COPY --chown=node . /src
WORKDIR /src
RUN cp -R /home/node/* /src/noteshrink/; rm /home/node/* -rf


# ADD HERE OCR LANGUAGES THAT YOU NEED
#RUN apt-get install -y tesseract-ocr-fin tesseract-ocr-swe

USER node
CMD ["node", "index.js"]
