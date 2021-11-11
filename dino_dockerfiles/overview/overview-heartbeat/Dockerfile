FROM golang:1.9.2-alpine3.7 as build

WORKDIR /src
ADD . /src/
RUN go build -o server


FROM alpine:3.7

EXPOSE 80

WORKDIR /app
COPY --from=build /src/server /app/

CMD [ "/app/server" ]
