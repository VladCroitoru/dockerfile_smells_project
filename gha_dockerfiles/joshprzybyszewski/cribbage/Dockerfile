# Start a base build with just go mod dependencies
FROM golang:1.14.3-alpine3.11 as base

ENV GOPATH=/go
WORKDIR $GOPATH/src/github.com/joshprzybyszewski/cribbage

# vendor'ed dependencies are unlikely to change, so download them first
COPY go.mod go.sum ./
RUN go mod download

# Create a separate image for the wasm files
FROM base as wasm

# Copy the specific directories/files we need to build the wasm binary
COPY utils utils
COPY model model
COPY network network
COPY jsonutils jsonutils
COPY wasm wasm

# Build the wasm output
RUN CGO_ENABLED=0 GOOS=js GOARCH=wasm go build -o /bin/wa_output.wasm github.com/joshprzybyszewski/cribbage/wasm

# Create a separate image for the server binary
FROM base as server

# Copy the specific directories/files we need to build the server binary
COPY logic logic
COPY jsonutils jsonutils
COPY utils utils
COPY model model
COPY network network
COPY server server
COPY main.go main.go

# Build the server's binary
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -tags prod -o /bin/cribbageServer main.go

# build environment
FROM node:14.3.0-alpine as react
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY client/package.json ./
COPY client/package-lock.json ./
RUN npm ci --silent
RUN npm install react-scripts@3.4.1 -g --silent
COPY client/ ./
RUN npm run build

# Start a new image that only holds the bare minimum files so that our image isn't too large
FROM scratch

WORKDIR /prod
COPY --from=server /tmp /tmp
COPY inis inis
COPY templates templates
COPY assets assets
COPY --from=react /app/build client/build/
COPY --from=wasm /bin/wa_output.wasm assets/wasm/wa_output.wasm
COPY --from=server /bin/cribbageServer .

# Define the gin server binary as the entry point
ENTRYPOINT ["/prod/cribbageServer"]