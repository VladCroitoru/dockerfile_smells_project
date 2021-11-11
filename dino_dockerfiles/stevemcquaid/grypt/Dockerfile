# First stage: build the executable.
FROM golang:1.12.5-alpine3.9 AS build_base

MAINTAINER Steve McQuaid <steve@stevemcquaid.com>

# Install the Certificate-Authority certificates for the app to be able to make
# calls to HTTPS endpoints.
# Git is required for fetching the dependencies.
RUN apk add --no-cache ca-certificates git

# Set the working directory outside $GOPATH to enable the support for modules.
WORKDIR /src



ADD ./go.mod /src/
COPY ./go.sum  /src/
RUN go mod download

# Import the code from the context.
COPY . /src



# Builder container
FROM build_base AS builder
# Build the executable to `/app`. Mark the build as statically linked.
RUN CGO_ENABLED=0 go build \
    -installsuffix 'static' \
    -o /app /src/



# Final stage: the running container.
FROM scratch AS final

## Import the user and group files from the first stage.
#COPY --from=builder /user/group /user/passwd /etc/

# Import the Certificate-Authority certificates for enabling HTTPS.
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

# Import the compiled executable from the first stage.
COPY --from=builder /app /app

## Declare the port on which the webserver will be exposed.
## As we're going to run the executable as an unprivileged user, we can't bind
## to ports below 1024.
#EXPOSE 5000

# Run the compiled binary.
ENTRYPOINT ["/app"]
