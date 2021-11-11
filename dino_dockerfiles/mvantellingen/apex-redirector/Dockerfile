# build stage
FROM golang:1.13-alpine AS build-env

WORKDIR /apexredirector

COPY . ./

ENV GOPROXY=https://proxy.golang.org
RUN go mod download
RUN go build -o apexredirector

# final stage
FROM alpine
RUN adduser -S apexredirector

USER apexredirector
WORKDIR /app
COPY --from=build-env /apexredirector/apexredirector /app

ENTRYPOINT ["./apexredirector"]

EXPOSE 8080 8443
