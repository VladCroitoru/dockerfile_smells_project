#### Configure these:
# Name of your binary.
ARG name=gotinyimg
# Path to base directory of the project, relative to "$GOPATH/src/".
ARG project=github.com/alcortesm/${name}
# Path to the directory of the main package, relative to "$GOPATH/src".
ARG main=${project}/cmd/${name}

####
# Creates a Docker image with the building tools required for compiling
# the project.
FROM golang:1.10.0 AS builder

# Adds the "dep" dependency manager.
RUN curl -fsSL \
    -o /usr/local/bin/dep \
    https://github.com/golang/dep/releases/download/v0.4.1/dep-linux-amd64 \
    && \
    chmod +x /usr/local/bin/dep

####
# Creates a Docker image with the source of the project and its
# dependencies, this will be used in the next stage to build the
# project, but can also be used externally to run the tests.
FROM builder AS src
ARG project

# installs dependencies
COPY Gopkg.toml Gopkg.lock /go/src/${project}/
WORKDIR /go/src/${project}
RUN dep ensure -vendor-only

# copy the project code
COPY . /go/src/${project}

####
# Compiles a static binary.
FROM src AS build
ARG name
ARG main

# Compile an static version of the main package.
RUN CGO_ENABLED=0 go build \
    -o /bin/${name} \
    -ldflags '-extldflags "-static"' \
    ${main}

####
# Create an small Docker image with the static binary and other required files.
FROM scratch AS run
ARG name

# Copy the timezone database, used by some stdlib packages like "time".
COPY --from=src \
    /usr/local/go/lib/time/zoneinfo.zip \
    /usr/local/go/lib/time/zoneinfo.zip

# Copy the SSL certificates, used by some stdlib packages like "http".
COPY --from=src \
    /etc/ssl/certs/ca-certificates.crt \
    /etc/ssl/certs/ca-certificates.crt

# Copy the binary generated in the previous build.
COPY --from=build \
    /bin/${name} \
    /runme
ENTRYPOINT [ "/runme" ]
