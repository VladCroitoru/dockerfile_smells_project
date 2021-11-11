FROM golang:1.16 as build
RUN apt update && apt install -y git
WORKDIR /app
COPY todoapp/go.mod .
COPY todoapp/go.sum .
RUN go mod download 
COPY todoapp .
RUN go build -o /out/app /app


FROM fedora
COPY --from=build /out/app /app
CMD ["/app"]
EXPOSE 8000