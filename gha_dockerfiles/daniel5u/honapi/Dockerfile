FROM golang:1.17-stretch

WORKDIR /app
COPY . ./
RUN go mod tidy
RUN go build -o /mainrun

EXPOSE 8080
CMD [ "/mainrun" ]