FROM python:alpine

RUN mkdir /root/.pip
ADD pip.conf /root/.pip/

RUN apk update \
    && apk add gcc g++ musl-dev python3-dev \
    && pip3 install pygments \
    && pip3 install requests \
    && pip3 install sphinx \
    && pip3 install mock \
    && pip3 install babel \
    && pip3 install curtsies \
    && pip3 install greenlet \
    && pip3 install urwid \
    && pip3 install bpython \
    && pip3 install numpy \
    && pip3 install ipython \
    && pip3 install ipdb \
    && pip3 install jupyter \
    && pip3 install pycodestyle \
    && pip3 install autopep8 \
    && apk del gcc musl-dev python3-dev \
    && rm -rf /root/.cache

CMD ["bpython"]
