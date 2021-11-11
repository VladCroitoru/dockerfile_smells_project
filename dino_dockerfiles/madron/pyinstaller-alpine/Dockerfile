FROM python:3.6.5-alpine3.7

ARG VERSION=3.3.1
RUN apk --no-cache add gcc musl-dev zlib-dev \
    && wget -O pyinstaller.tgz https://github.com/pyinstaller/pyinstaller/releases/download/v$VERSION/PyInstaller-$VERSION.tar.gz \
    && mkdir pyinstaller \
    && cd pyinstaller; tar xfz ../pyinstaller.tgz --strip-components=1 \
    && cd /pyinstaller/bootloader; python3 ./waf configure --no-lsb all \
    && cd /pyinstaller/bootloader; pip3 install .. \
    && apk del musl-dev zlib-dev \
    && rm -rf /pyinstaller*
