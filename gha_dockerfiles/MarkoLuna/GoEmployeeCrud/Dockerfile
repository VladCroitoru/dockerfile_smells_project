FROM golang:alpine

WORKDIR /dist

COPY app main
COPY resources/ssl ssl

EXPOSE 8080

CMD ["/dist/main"]

# docker build -t goemployee_crud .