# FROM golang:1.16-buster as build
# # try to modidy this route /go/src/measure   dont focus on measure
# WORKDIR /go/src/measure
# ADD . .

# RUN go mod download
# RUN go build -o /go/main

# FROM gcr.io/distroless/base-debian10
# WORKDIR /go/
# COPY --from=build /go/main .

# # EXPOSE 8080

# CMD ["./main"]

# FROM golang:1.16-alpine
# WORKDIR /src
# ADD . /src
# RUN pwd
# RUN go mod download
# RUN go build main.go
# CMD ["./main"]

FROM golang:1.16-alpine
WORKDIR /src
ADD . /src
RUN pwd
RUN go build -mod vendor main.go
CMD ["./main"]
