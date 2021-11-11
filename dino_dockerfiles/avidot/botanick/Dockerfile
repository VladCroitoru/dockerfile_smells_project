############################################
# director v0.1
# author: Adrien VIDOT
# url: 
############################################

FROM ubuntu:latest
MAINTAINER Adrien VIDOT <avidot@squad.pro>

RUN \
  apt-get update && \
  apt-get -y upgrade  && \
  apt-get install -y \
    python3 \
      python3-pip \
      python3-dev \
      build-essential

RUN mkdir /app
COPY ./requirements.txt /app
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./botanick /app/botanick
ENV PYTHONIOENCODING=UTF-8

ENTRYPOINT ["python3"]
CMD ["/app/botanick/Botanick.py"]
