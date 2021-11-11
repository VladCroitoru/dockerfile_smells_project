FROM golang:1.6-alpine

MAINTAINER Jim Mar <majinjing3@gmail.com>
ENV CREATE_DATE 2016-05-03

ENV TIDY_DIR /usr/local/tidy
ENV BUILD_DIR /go/src/github.com/jim3mar/tidy
ENV BUILDTAGS debug
ENV GOPATH /go

ADD . ${BUILD_DIR}

RUN cd ${BUILD_DIR} && \
      CGO_ENABLED=0 go install -tags '$(BUILDTAGS)' . && \
      mkdir -p ${TIDY_DIR}/tmp && \
      cp ${GOPATH}/bin/tidy ${TIDY_DIR}/ && \
      cp -vfr keys ${TIDY_DIR}/ && \
  	  cp -vfr tidy.yaml ${TIDY_DIR}/ && \
      apk --no-cache add openssl && \
      (cd ${TIDY_DIR}/keys/; sh ${TIDY_DIR}/keys/key-gen.sh) && \
      rm -rf GOPATH

WORKDIR /usr/local/tidy/

EXPOSE 8089

CMD ["/usr/local/tidy/tidy"]
