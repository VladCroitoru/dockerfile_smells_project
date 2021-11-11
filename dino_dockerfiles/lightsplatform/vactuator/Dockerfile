# Build stage
FROM golang:alpine AS build-env
COPY . $GOPATH/src/github.com/LightsPlatform/vActuator
RUN apk update && apk add git
WORKDIR $GOPATH/src/github.com/LightsPlatform/vActuator
RUN go get -v && go build -v -o /vActuator

# Final stage
FROM python:3-alpine
EXPOSE 8181/tcp
WORKDIR /app
COPY --from=build-env /vActuator /app/
COPY runtime.py /app/runtime.py
RUN cd /app/runtime.py && python3 setup.py install
ENTRYPOINT ["./vActuator"]
