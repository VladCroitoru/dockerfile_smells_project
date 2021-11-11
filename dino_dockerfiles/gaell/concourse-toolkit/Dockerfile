FROM golang:1.12 AS build-env
RUN apt-get install make
ADD . /go/concourse-toolkit
RUN cat /go/concourse-toolkit/TAG
RUN cd /go/concourse-toolkit && ./docker-build.sh

FROM scratch
COPY --from=build-env /go/bin/concourse-toolkit /bin/concourse-toolkit
ENTRYPOINT ["/bin/concourse-toolkit"]
