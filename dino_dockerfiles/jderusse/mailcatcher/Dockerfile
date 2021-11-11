FROM ruby:alpine

RUN apk add --no-cache \
        sqlite-libs

RUN apk add --no-cache --virtual .build-deps \
        build-base \
        sqlite-dev \
 && gem install mailcatcher --no-document \
 && apk del .build-deps

EXPOSE 80
EXPOSE 25

CMD ["--smtp-port", "25", "--http-port", "80", "--ip", "0.0.0.0", "-f"]
ENTRYPOINT ["mailcatcher"]
