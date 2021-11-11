FROM ubuntu
# includes Python 3.8.5

# Linux Updates
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get upgrade -y

# Sysytem Depencencies
ENV PYTHONUNBUFFERED=1
RUN apt-get -yqq install python3-pip python3-dev
RUN apt-get -y install poppler-utils --fix-missing
RUN apt-get -y install tesseract-ocr
RUN python3 -m pip install --upgrade pip

# App Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app app
COPY .env .env

# Network Settings
EXPOSE 8000
CMD uvicorn app.main:app --host 0.0.0.0 --port 8000
