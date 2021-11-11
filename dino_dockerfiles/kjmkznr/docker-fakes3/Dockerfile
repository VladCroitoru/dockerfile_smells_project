FROM alpine:3.7
ENV FAKES3_VERSION=1.2.1
WORKDIR /fakes3

RUN apk add --no-cache ruby ruby-io-console
RUN gem install fakes3 -v $FAKES3_VERSION --no-doc
RUN mkdir -p /fakes3 && chown nobody:nobody /fakes3 && chmod 0750 /fakes3

USER nobody
EXPOSE 4567
CMD ["fakes3", "-r",  "/fakes3", "-p",  "4567"]
