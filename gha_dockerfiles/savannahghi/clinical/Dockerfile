# Use the official Golang image to create a build artifact.
# This is based on Debian and sets the GOPATH to /go.
# https://hub.docker.com/_/golang
FROM golang:1.16 as builder

# Create and change to the app directory.
WORKDIR /app

# Copy go.sum/go.mod and warm up the module cache (so that this
# rather long step can be cached if go.mod/go.sum don't change)
COPY go.* $D/
CMD go mod download

# Now copy the rest.
COPY . /app/

# Retrieve application dependencies.
RUN go mod download

# Build the binary.
RUN cd /app/ && CGO_ENABLED=0 GOOS=linux go build -v -o server github.com/savannahghi/clinical

# Use the official Alpine image for a lean production container.
# https://hub.docker.com/_/alpine
# https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds
FROM alpine:3
RUN apk add --no-cache ca-certificates

# Copy the binary to the production image from the builder stage.
COPY --from=builder /app/server /server
COPY --from=builder /app/deps.yaml /deps.yaml

COPY --from=builder /app/graph/clinical/rbac_model.conf /app/graph/clinical/rbac_model.conf
COPY --from=builder /app/graph/clinical/data/rbac_policy.csv /app/graph/clinical/data/rbac_policy.csv

# Run the web service on container startup.
CMD ["/server"]
