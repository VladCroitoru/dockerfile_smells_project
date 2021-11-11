# Accept the Go version for the image to be set as a build argument.
ARG GO_VERSION=1.15
# First stage: build the executable.
FROM golang:${GO_VERSION}-alpine AS builder

ARG VERSION=""
ARG BRANCH=""
ARG COMMIT=""


# Create the user and group files that will be used in the running container to
# run the process as an unprivileged user.
RUN mkdir /user && \
    echo 'nobody:x:65534:65534:nobody:/:' > /user/passwd && \
    echo 'nobody:x:65534:' > /user/group

# Install the Certificate-Authority certificates for the app to be able to make
# calls to HTTPS endpoints.
# Git is required for fetching the dependencies.
RUN apk add --no-cache ca-certificates git

# Set the working directory outside $GOPATH to enable the support for modules.
WORKDIR /src

# Fetch dependencies first; they are less susceptible to change on every build
# and will therefore be cached for speeding up the next build
COPY ./go.mod ./go.sum ./
RUN go mod download

# Import the code from the context.
COPY ./ ./ 

# Build the executable to `/app`. Mark the build as statically linked.
RUN CGO_ENABLED=0 go build \
    -installsuffix 'static' \
    -ldflags "-X main.Revision=${COMMIT} \
        -X main.Branch=${BRANCH} \
        -X main.Version=${VERSION} \
        -X main.BuildDate=$(date -u ""+%Y%m%d-%H:%M:%S"")" \
    -o /app .

# Final stage: the running container.
FROM scratch AS final

# Add maintainer label in case somebody has questions.
LABEL maintainer="Kris.Budde@gmail.com"

# Import the user and group files from the first stage.
COPY --from=builder /user/group /user/passwd /etc/

# Import the Certificate-Authority certificates for enabling HTTPS.
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

# Import the compiled executable from the first stage.
COPY --from=builder /app /app

# Declare the port on which the webserver will be exposed.
# As we're going to run the executable as an unprivileged user, we can't bind
# to ports below 1024.
EXPOSE 9419

# Perform any further action as an unprivileged user.
USER nobody:nobody

# Check if exporter is alive; 10 retries gives prometheus some time to retrieve bad data (5 minutes)
HEALTHCHECK --retries=10 CMD ["/app", "-check-url", "http://localhost:9419/health"]
# Run the compiled binary.
ENTRYPOINT ["/app"]
