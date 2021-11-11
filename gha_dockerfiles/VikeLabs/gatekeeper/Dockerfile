FROM golang:1.15.6-alpine as builder
LABEL maintainer="VikeLabs <gatekeeper@vikelabs.ca>"

WORKDIR /app
COPY go.mod go.sum ./

RUN go mod download
# copy source code
COPY . .
# build application
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

FROM scratch
WORKDIR /root/

# Copy the Pre-built binary file from the build stage
COPY --from=builder /app/main .

ENV BOT_TOKEN=""

CMD ["./main"]