FROM golang:1.17.0-stretch AS build
WORKDIR /src
COPY . .
# Static build required so that we can safely copy the binary over.
RUN CGO_ENABLED=0 go build -ldflags '-extldflags "-static"' -o /out/xuitecrawler cmd/main.go

FROM scratch AS bin
COPY --from=build /out/xuitecrawler /out/xuitecrawler
