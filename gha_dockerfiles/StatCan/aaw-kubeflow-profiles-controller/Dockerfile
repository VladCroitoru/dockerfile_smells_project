# Build with the golang image
FROM golang:1.16-alpine AS build

# Add git
RUN apk add git

# Set workdir
WORKDIR /src

# Add dependencies
COPY go.mod .
COPY go.sum .
RUN go mod download

# Build
COPY . .
RUN CGO_ENABLED=0 go install .

# Generate final image
FROM alpine:3.14
RUN apk --update --no-cache add ca-certificates
COPY --from=build /go/bin/profiles-controller /usr/local/bin/profiles-controller
ENTRYPOINT [ "/usr/local/bin/profiles-controller" ]
