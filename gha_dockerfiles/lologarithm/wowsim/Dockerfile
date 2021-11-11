FROM golang:1.15.7

# Set up working directory and copy everything to the container
WORKDIR /go/src/app
COPY . .

# Install dependencies
RUN go get -d -v ./...
RUN go install -v ./...

# Build server and ui
RUN GOOS=linux GOARCH=amd64 go build .
RUN GOOS=js GOARCH=wasm go build -o ui/lib.wasm ui/main_wasm.go

EXPOSE 3333

# Run the dev server
CMD go run main.go web.go --web
