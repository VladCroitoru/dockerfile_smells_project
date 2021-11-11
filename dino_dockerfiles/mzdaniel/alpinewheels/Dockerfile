FROM alpine
MAINTAINER Daniel Mizyrycki mzdaniel@glidelink.net

ENV WHEELS='pillow psycopg2 gevent'
ENV PKGS='python python3 curl alpine-sdk python-dev python3-dev postgresql-dev libjpeg-turbo-dev zlib-dev libffi-dev openssl-dev'

ENV LIBRARY_PATH=/lib:/usr/lib

RUN\
     # Install packages
     apk update  &&\
     apk add $PKGS  &&\
     curl https://bootstrap.pypa.io/get-pip.py | python  &&\
     pip install wheel  &&\
     pip3 install -U pip; pip3 install wheel  &&\

     # Build psycopg2 wheel
     for w in $WHEELS; do \
         pip2 wheel $w; pip3 wheel $w; done  &&\

     # Cleanup
     apk del $PKGS  &&\
     rm -rf /var/cache/apk/* /root/.cache /tmp/*  &&\
     find /usr/lib/python2.7 -name '*pyo' -exec rm {} \;  &&\

     echo -e '\nsha1 checksum for wheel verification:'  &&\
     sha1sum /*.whl

