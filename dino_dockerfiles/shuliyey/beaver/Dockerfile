FROM alpine:3.5

RUN apk add --update python py-pip \
  && pip install --upgrade pip \
  && pip install --upgrade beaver \
  && rm -rf /var/cache/apk/*

RUN mkdir -p /opt/beaver
WORKDIR /opt/beaver

COPY beaver.conf /opt/beaver/

VOLUME /opt/beaver

CMD ["/usr/bin/beaver", "-c","/opt/beaver/beaver.conf"]
