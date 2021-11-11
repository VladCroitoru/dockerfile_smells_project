############################
# STEP 1 build executable binary
############################
FROM golang:1.13-alpine as builderGo
# Install git + SSL ca certificates.
# Git is required for fetching the dependencies.
# Ca-certificates is required to call HTTPS endpoints.
RUN apk update && apk add --no-cache git ca-certificates
# Create appuser
RUN adduser -D -g '' appuser
# Copy the go source
COPY ./*.go $GOPATH/src/github.com/stevenweathers/Movie-UPC-API/
COPY ./go.mod $GOPATH/src/github.com/stevenweathers/Movie-UPC-API/
COPY ./go.sum $GOPATH/src/github.com/stevenweathers/Movie-UPC-API/
# Set working dir
WORKDIR $GOPATH/src/github.com/stevenweathers/Movie-UPC-API/
# Fetch dependencies.
RUN go mod download
# Build the binary
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -installsuffix cgo -ldflags="-w -s" -o /go/bin/movie-upc-api

############################
# STEP 2 build a small image
############################
FROM scratch
# Import from builder.
COPY --from=builderGo /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builderGo /etc/passwd /etc/passwd
# Copy our static executable
COPY --from=builderGo /go/bin/movie-upc-api /go/bin/movie-upc-api
# Use an unprivileged user.
USER appuser

# Run the movie-upc-api binary.
ENTRYPOINT ["/go/bin/movie-upc-api"]