FROM alpine:3.2

RUN apk add --update py-pip python \
    && pip install -U pip \
    && rm -rf /var/cache/apk/* \
    && ln -s /usr/etc/tvrenamer /etc/tvrenamer

COPY . /tvrenamer/

WORKDIR /tvrenamer

RUN apk add --update git g++ python-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && python setup.py install \
    && apk del git g++ python-dev \
    && rm -rf /var/cache/apk/* .git/ build/ *.egg-info/

VOLUME ["/usr/etc/tvrenamer"]

CMD ["tvrename"]

