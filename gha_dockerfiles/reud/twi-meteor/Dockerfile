# use a first-stage image to build the go code
# we'll change it later
FROM golang:1.16 AS build

RUN mkdir /go-app
WORKDIR /go-app
# for now we only need the go code
COPY . .
RUN go mod download

# build a standalone executable
RUN CGO_ENABLED=0 go build -o /app main.go

# switch to a second-stage production image
FROM couchbase

# copy the executable from the first stage
# into the production image
COPY --from=build /app /app
COPY .env .env

CMD ["/app"]