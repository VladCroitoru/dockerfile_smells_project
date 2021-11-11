FROM golang:1.17.0
WORKDIR /app
ADD *.go .
ADD go.mod .
ADD go.sum .
RUN CGO_ENABLED=0 GOOS=linux go build -o main .

FROM scratch
WORKDIR /app
COPY --from=0 /app/main .
COPY index.html .
CMD ["/app/main"]
EXPOSE 8000
