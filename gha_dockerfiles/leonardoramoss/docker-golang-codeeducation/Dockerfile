FROM golang:1.17-alpine AS build
WORKDIR /build
COPY ./hello.go ./
RUN go build ./hello.go

FROM scratch
COPY --from=build /build/hello .
ENTRYPOINT ["./hello"]