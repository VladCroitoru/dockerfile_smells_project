# Build stage
FROM golang:alpine AS build-env
COPY . $GOPATH/src/github.com/LightsPlatform/vSensor
RUN apk update && apk add git
WORKDIR $GOPATH/src/github.com/LightsPlatform/vSensor
RUN go get -v && go build -v -o /vSensor

# Final stage
FROM python:3-alpine
EXPOSE 8080/tcp
WORKDIR /app
COPY --from=build-env /vSensor /app/
COPY runtime.py /app/runtime.py
RUN cd /app/runtime.py && python3 setup.py install
ENTRYPOINT ["./vSensor"]
