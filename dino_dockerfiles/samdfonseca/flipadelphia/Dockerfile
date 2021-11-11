FROM golang:1.7

COPY . /go/src/app
RUN mkdir -p /go/src/github.com/samdfonseca/ && \
    mv /go/src/app/ /go/src/github.com/samdfonseca/flipadelphia && \
    cd /go/src/github.com/samdfonseca/flipadelphia && \
    GLIDE_OS_ARCH=$(go env GOHOSTOS)-$(go env GOHOSTARCH) && \
    GLIDE_TAG=$(curl -s https://glide.sh/version) && \
    GLIDE_LATEST_RELEASE_URL="https://github.com/Masterminds/glide/releases/download/${GLIDE_TAG}/glide-${GLIDE_TAG}-${GLIDE_OS_ARCH}.tar.gz" && \
    wget ${GLIDE_LATEST_RELEASE_URL} -O /tmp/glide.tar.gz && \
    mkdir /tmp/glide && \
    tar --directory=/tmp/glide -xvf /tmp/glide.tar.gz && \
    /tmp/glide/${GLIDE_OS_ARCH}/glide install && \
    mkdir -p ${HOME}/.flipadelphia && \
    cp ./config/config.example.json ${HOME}/.flipadelphia/config.json && \
    make build && \
    make install

ENV FLIPADELPHIA_ENV=bolt
EXPOSE 3006
ENTRYPOINT ["flipadelphia", "&"]
