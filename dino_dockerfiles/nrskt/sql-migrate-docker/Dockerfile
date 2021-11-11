FROM golang:1.9.1

RUN go get github.com/rubenv/sql-migrate/...

ENTRYPOINT ["sql-migrate"]
CMD ["--help"]