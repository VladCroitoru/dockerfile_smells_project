ARG        GO_VERSION=1.11.5

# Builder image
FROM       golang:${GO_VERSION} as builder

ARG        BUILD_DATE
ARG        REPO_BRANCH
ARG        REPO_VERSION
ARG        VERSION

COPY       .  /go/src/app/
WORKDIR    /go/src/app
RUN        go get -u github.com/golang/dep/cmd/dep && \
           dep ensure && \
           CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o eatr -ldflags "-X main.version=${VERSION} -X main.repoBranch=${REPO_BRANCH} -X main.repoVersion=${REPO_VERSION}" .


# Final image
# For an explanation of why we need to repeat the ARGs, see https://github.com/moby/moby/issues/34129
# Also needed to copy the CA certifictes to scratch as it has no content and the AWS package calls will fail
FROM       scratch

ARG        BUILD_DATE
ARG        REPO_BRANCH
ARG        REPO_VERSION
ARG        VERSION

# See http://label-schema.org/rc1/
LABEL      org.label-schema.build-date=$BUILD_DATE \
           org.label-schema.schema-version="1.0" \
           org.label-schema.vcs-branch=$REPO_BRANCH \
           org.label-schema.vcs-ref=$REPO_VERSION \
           org.label-schema.version=$VERSION

COPY       --from=builder /go/src/app/eatr .
COPY       --from=builder /etc/ssl/certs/ca-certificates.crt  /etc/ssl/certs/ca-certificates.crt

EXPOSE     5000
ENTRYPOINT ["/eatr"]
