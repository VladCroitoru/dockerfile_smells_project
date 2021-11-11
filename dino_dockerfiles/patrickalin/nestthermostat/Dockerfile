FROM golang:1.6-alpine
RUN apk add --no-cache --virtual .build-deps git
WORKDIR /go/src/
RUN git clone https://github.com/patrickalin/GoNestThermostatAPIRest.git
WORKDIR /go/src/GoNestThermostatAPIRest
RUN go get
RUN go build
COPY config.yaml /go/src/GoNestThermostatAPIRest/config.yaml
RUN chmod 777 /go/src/GoNestThermostatAPIRest
ENTRYPOINT /go/src/GoNestThermostatAPIRest/GoNestThermostatAPIRest
