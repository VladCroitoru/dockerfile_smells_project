FROM alpine:3.4

MAINTAINER tf.pack@gmail.com

RUN apk update && \
    apk upgrade && \
    apk add \
          nodejs \
          git
RUN git clone https://github.com/hakimel/reveal.js.git /opt/revealjs
RUN npm install -g http-server

COPY slides /opt/revealjs
WORKDIR /opt/revealjs

EXPOSE 8080

ENTRYPOINT ["http-server"]