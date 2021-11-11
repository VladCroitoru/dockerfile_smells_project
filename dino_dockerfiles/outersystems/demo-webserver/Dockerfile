FROM golang as bin

WORKDIR /go/src/app
COPY . .

RUN CGO_ENABLED=0 GOOS=linux go build -a -tags netgo -ldflags '-w' .

FROM scratch
COPY --from=bin /go/src/app/app /usr/local/bin/app
COPY --from=bin /etc/passwd /etc/passwd
USER nobody
ENTRYPOINT ["app"]
