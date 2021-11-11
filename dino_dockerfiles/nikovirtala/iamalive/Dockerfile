FROM golang:alpine as build

ADD . /root/
WORKDIR /root
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o iamalive .

FROM gcr.io/distroless/base
LABEL maintainer "Niko Virtala <niko@nikovirtala.io>"

WORKDIR /
COPY --from=build /root/iamalive .
COPY --from=build /root/test.gtpl .
EXPOSE 80
ENTRYPOINT ["/iamalive"]
