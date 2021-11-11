# build stage
FROM golang AS build-env
ADD . /go/src/github.com/AlekSi/telesock
RUN cd /go/src/github.com/AlekSi/telesock && env CGO_ENABLED=0 go build -v -o /telesock

# final stage
FROM scratch
COPY --from=build-env /telesock /telesock
EXPOSE 1080
ENTRYPOINT ["/telesock"]
