# download dependencies:
# make and bash to run the Makefile
# nodejs to run client wasm tests
# aspell and aspell-en for game word list
# download go dependencies for source code
FROM golang:1.17-alpine3.13 AS BUILDER
WORKDIR /app
COPY go.mod go.sum ./
RUN apk add --no-cache \
        make=~4.3 \
        bash=~5.1 \
        nodejs=~14 \
        aspell=~0.60 \
        aspell-en=2020.12.07-r0 \
    && go mod download

# build the server, delete build cache
COPY . ./
RUN make build/selene-bananas \
        GO_ARGS="CGO_ENABLED=0" \
    && go clean -cache

# copy the server to a minimal build image
FROM scratch
WORKDIR /app
COPY --from=BUILDER app/build/selene-bananas ./
ENTRYPOINT [ "/app/selene-bananas" ]
