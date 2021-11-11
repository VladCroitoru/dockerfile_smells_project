
# Copyright Red Hat

FROM registry.ci.openshift.org/open-cluster-management/builder:go1.16-linux AS builder

ENV REMOTE_SOURCE='.'
ENV REMOTE_SOURCE_DIR='/remote-source'

COPY $REMOTE_SOURCE $REMOTE_SOURCE_DIR/app/
WORKDIR $REMOTE_SOURCE_DIR/app
COPY go.mod go.mod
COPY go.sum go.sum
# cache deps before building and copying source so that we don't need to re-download as much
# and so that source changes don't invalidate our downloaded layer
# RUN go mod download

RUN GOFLAGS="" go build -a -o idp-mgmt main.go

RUN GOFLAGS="" go test -covermode=atomic \
    -coverpkg=github.com/identitatem/idp-mgmt-operator/pkg/...,\
github.com/identitatem/idp-mgmt-operator/controllers/... \
     -c -tags testrunmain \ 
     github.com/identitatem/idp-mgmt-operator/cmd/manager \
     -o idp-mgmt-coverage

FROM registry.access.redhat.com/ubi8/ubi-minimal:latest
RUN microdnf update
ENV REMOTE_SOURCE_DIR='/remote-source'

ENV OPERATOR=/usr/local/bin/idp-mgmt \
    USER_UID=1001 \
    USER_NAME=idp-mgmt-operator
    
# install operator binary
COPY --from=builder $REMOTE_SOURCE_DIR/app/idp-mgmt ${OPERATOR}
COPY --from=builder $REMOTE_SOURCE_DIR/app/idp-mgmt-coverage ${OPERATOR}-coverage
COPY --from=builder $REMOTE_SOURCE_DIR/app/build/bin /usr/local/bin

RUN  /usr/local/bin/user_setup

ENTRYPOINT ["/usr/local/bin/entrypoint"]

USER ${USER_UID}
