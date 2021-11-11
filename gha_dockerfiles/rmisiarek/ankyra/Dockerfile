FROM golang:1.17 AS build

WORKDIR /src/
COPY go.mod *.go /src/

RUN CGO_ENABLED=0 go build -o /bin/ankyra-service

FROM scratch
COPY --from=build /bin/ankyra-service /bin/ankyra-service

EXPOSE 8080

ENTRYPOINT ["/bin/ankyra-service"]
