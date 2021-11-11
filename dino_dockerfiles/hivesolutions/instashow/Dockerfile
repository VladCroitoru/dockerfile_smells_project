FROM hivesolutions/python:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

EXPOSE 8080

ENV LEVEL INFO
ENV SERVER netius
ENV SERVER_ENCODING gzip
ENV HOST 0.0.0.0
ENV PORT 8080
ENV INSTAGRAM_ID INSTAGRAM_ID
ENV INSTAGRAM_SECRET INSTAGRAM_SECRET
ENV INSTAGRAM_REDIRECT_URL INSTAGRAM_REDIRECT_URL
ENV TITLE Instashow
ENV SUB_TITLE Slideshow
ENV PYTHONPATH /src

ADD requirements.txt /
ADD src /src

RUN pip3 install -r /requirements.txt && pip3 install --upgrade netius

CMD ["/usr/bin/python3", "/src/instashow/main.py"]
