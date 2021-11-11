FROM alpine:3.7

# Switch to edge (for latest firefox)
RUN sed -i -e 's/v[[:digit:]]\.[[:digit:]]/edge/g' /etc/apk/repositories
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
RUN apk update && apk upgrade

RUN apk add firefox python3 jq curl
RUN rm -rf /var/cache/apk/*

COPY docker/geckodriver.sh geckodriver.sh
RUN sh geckodriver.sh

COPY . /usr/src/app
RUN pip3 install /usr/src/app

WORKDIR /root
RUN rm -rf /usr/src/app
COPY /docker/run.sh /root/run.sh

CMD /root/run.sh
