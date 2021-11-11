FROM ubuntu:latest
MAINTAINER Matthieu Serrepuy "lotooo@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["plex2hue.py"]
