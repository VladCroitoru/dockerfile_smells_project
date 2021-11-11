# Dockerfile References: https://docs.docker.com/engine/reference/builder/

# Start from the latest golang base image
FROM golang:1.15 as builder

# Set the Current Working Directory inside the container
WORKDIR /app

# Fetch dependencies first; they are less susceptible to change on every build
# and will therefore be cached for speeding up the next build
COPY ./go.mod ./

RUN go mod download
RUN go get -u github.com/swaggo/swag/cmd/swag
RUN go get -u github.com/swaggo/gin-swagger
RUN go get -u github.com/swaggo/files

# Copy everything from the current directory to the Working Directory inside the container
COPY . .

RUN swag init

# Build the Go app
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

######## Start a new stage from scratch #######
FROM alpine:latest

RUN apk --no-cache add ca-certificates tzdata

WORKDIR /root/

# Copy the Pre-built binary file from the previous stage
COPY --from=builder /app/main .

# Add files to the image
ADD config config

# Expose port 8080 to the outside world
EXPOSE 8080

# Command to run the executable
CMD ["./main"]

