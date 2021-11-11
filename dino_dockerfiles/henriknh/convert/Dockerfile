FROM alpine:latest
RUN apk update

ADD convert.py convert.py

RUN apk --no-cache add \
    ffmpeg \
    python3

RUN pip3 install \
    pyinotify

ENTRYPOINT ["python3", "convert.py"]
