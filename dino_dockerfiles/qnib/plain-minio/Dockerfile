ARG DOCKER_REGISTRY=docker.io
ARG FROM_IMG_REPO=qnib
ARG FROM_IMG_NAME="alplain-golang"
ARG FROM_IMG_TAG="1.10.3"
ARG FROM_IMG_HASH=""
FROM ${DOCKER_REGISTRY}/${FROM_IMG_REPO}/${FROM_IMG_NAME}:${FROM_IMG_TAG}${DOCKER_IMG_HASH} AS build

ARG MINIO_REL=2018-07-23T18-34-49Z

RUN apk add --update git musl-dev
WORKDIR /usr/local/src/github.com/minio/
RUN git clone https://github.com/minio/minio.git ./minio
WORKDIR /usr/local/src/github.com/minio/minio
RUN git checkout tags/RELEASE.${MINIO_REL}
RUN go build

FROM qnib/alplain-init
ENV MINIO_DATA=/data/
COPY --from=build /usr/local/src/github.com/minio/minio/minio /usr/local/bin/
COPY opt/qnib/minio/bin/start.sh /opt/qnib/minio/bin/
CMD ["/opt/qnib/minio/bin/start.sh"]
