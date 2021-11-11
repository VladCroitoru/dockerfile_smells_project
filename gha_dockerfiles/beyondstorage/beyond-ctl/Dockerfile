FROM golang:1.16 AS build

WORKDIR /app
COPY . ./

RUN CGO_ENABLED=0 go build -o /beyondctl ./cmd/beyondctl

FROM scratch

WORKDIR /

COPY --from=build /beyondctl /beyondctl

ENTRYPOINT ["/beyondctl"]
