FROM golang:1.16 as build

WORKDIR /go/src/app
COPY . .

RUN CGO_ENABLED=0 go build -installsuffix nocgo -o app-bin .

FROM scratch
COPY  --from=build /go/src/app/app-bin ./
ENTRYPOINT ["./app-bin"]