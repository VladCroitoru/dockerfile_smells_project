FROM golang:alpine

# Set necessary environmet variables needed for our image
ENV GO111MODULE=on \
    CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64 \
    GOPATH=/mnt/

# Move to working directory /build
WORKDIR /mnt/src/github.com/web_crawler

# Copy and download dependency using go mod
COPY go.mod .
COPY go.sum .
# RUN go mod download
RUN go mod tidy
RUN go mod vendor

# Copy the code into the container
COPY . .

# Build the application
RUN go build -o web_crawler .

# Move to /dist directory as the place for resulting binary folder
WORKDIR /dist

# Copy binary from build to main folder
RUN cp /mnt/src/github.com/web_crawler/web_crawler .

# Export necessary port
EXPOSE 9000

# Command to run when starting the container
CMD ["/dist/web_crawler"]