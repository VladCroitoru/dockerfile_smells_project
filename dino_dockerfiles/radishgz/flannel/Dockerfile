FROM gcr.io/google_containers/kube-cross:v1.6.2-2

ENV CC=gcc
ENV GOARM=6
ENV GOARCH=amd64
#ENV 
#docker run -e CC=$(CC) -e GOARM=$(GOARM) -e GOARCH=$(ARCH) \
#	-u $(shell id -u):$(shell id -g) \
#COPY .   /go/src/github.com/coreos/flannel

#	    -v ${PWD}:/go/src/github.com/coreos/flannel:ro \
#        -v ${PWD}/dist:/go/src/github.com/coreos/flannel/dist \
#	    gcr.io/google_containers/kube-cross:$(KUBE_CROSS_TAG) /bin/bash -c '\

#RUN mkdir -p /go/src/github.com/coreos/flannel/dist
#RUN go get ./...

#RUN		cd /go/src/github.com/coreos/flannel && \#
#		CGO_ENABLED=1 make -e dist/flanneld && \
#		mv dist/flanneld dist/flanneld-$ARCH && \
#		file dist/flanneld-$ARCH
