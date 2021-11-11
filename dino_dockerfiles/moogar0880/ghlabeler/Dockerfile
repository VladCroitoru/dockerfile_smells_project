FROM golang:1.6.3-alpine

COPY . /go/src/github.com/moogar0880/ghlabeler

RUN apk add --update git && \
      go get github.com/Masterminds/glide && \
      cd /go/src/github.com/moogar0880/ghlabeler && \
      glide install && \
      go install github.com/moogar0880/ghlabeler/cmd/ghlabels

ENTRYPOINT ["/go/bin/ghlabels"]
CMD ["-h"]
