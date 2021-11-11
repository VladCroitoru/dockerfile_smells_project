FROM python:2.7-slim

ENV DEBIAN_FRONTEND noninteractive

COPY app.py /opt/app.py

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libfreetype6-dev libjpeg62-turbo-dev liblcms2-dev libtiff5-dev libwebp-dev libwebpdemux1 libwebpmux1 zlib1g-dev && \
    ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib && \
    ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib && \
    ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib && \
    pip install Pillow

CMD [ "python", "-u", "/opt/app.py" ]
