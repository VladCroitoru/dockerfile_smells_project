FROM ubuntu:latest

# Install base packages
RUN apt-get update \
  && apt-get dist-upgrade -y \
  && apt-get install -y tesseract-ocr tesseract-ocr-eng imagemagick ghostscript poppler-utils ruby python python-pip
RUN pip install --upgrade pip && pip install pypdfocr

RUN mkdir /app
COPY process /app/process
COPY sort-by-filename /app/sort-by-filename
RUN chmod +x /app/*

ENTRYPOINT /app/process /source /destination
