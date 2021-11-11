# syntax=docker/dockerfile:1

### Build Stage ###
# Choose a good base image for building: buster.
# The HTTP server uses SQLite which is an embedded C library, and buster has gcc compiler installed.
FROM golang:1.16-buster AS build-env

# Copy source files.
WORKDIR /app
ADD . /app

# Resolve dependencies.
RUN go mod vendor

# Compile to binary, target Linux so that Docker can run it everywhere.
RUN GOOS=linux go build -o /app/cncamp_http_server

### Final Stage ###
# Choose one of the smallest base images: distroless.
FROM gcr.io/distroless/base-debian10

# Copy the binary file.
COPY --from=build-env /app/cncamp_http_server /

EXPOSE 8080
CMD [ "/cncamp_http_server" ]
