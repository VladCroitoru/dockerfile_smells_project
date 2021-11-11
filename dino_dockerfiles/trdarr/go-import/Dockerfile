FROM golang:1.9-alpine AS build

WORKDIR /go/src/app
RUN mkdir -p /go/src/app
COPY index.gohtml main.go ./
RUN go build


FROM alpine

WORKDIR /app
COPY --from=build /go/src/app .
ENTRYPOINT ["./app"]
EXPOSE 80
