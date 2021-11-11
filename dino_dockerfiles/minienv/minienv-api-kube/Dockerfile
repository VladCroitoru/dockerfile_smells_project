FROM golang:latest

RUN mkdir -p /go/src/app
WORKDIR /go/src/app
ADD . /go/src/app/ 
RUN go get -v -d \
  && CGO_ENABLED=0 GOOS=linux go install -a -installsuffix cgo app

FROM alpine:latest
MAINTAINER Mark Watson <markwatsonatx@gmail.com>
COPY --from=0 /go/bin/app /app
COPY env-pv-host-path.yml \
     env-pvc-host-path.yml \
     env-pvc-storage-class.yml \
     env-deployment.yml \
     env-service.yml \
     provisioner-job.yml /
CMD ["/app", "80"]
