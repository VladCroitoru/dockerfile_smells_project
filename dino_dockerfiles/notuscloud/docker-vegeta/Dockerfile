FROM alpine as build
RUN apk update && apk add curl
RUN mkdir /workdir
WORKDIR /workdir
RUN curl -O -L https://github.com/tsenart/vegeta/releases/download/v6.3.0/vegeta-v6.3.0-linux-amd64.tar.gz
RUN tar xf vegeta-v6.3.0-linux-amd64.tar.gz

FROM alpine
COPY --from=build /workdir/vegeta /bin/vegeta
CMD ["vegeta"]

