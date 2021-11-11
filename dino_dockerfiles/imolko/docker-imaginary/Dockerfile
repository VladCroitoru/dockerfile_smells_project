FROM alpine:3.6 as builder

ARG VIPS_VERSION=8.5.6
ARG IMAGINARY_VERSION=1.0.5

ENV GOROOT=/usr/lib/go \
    GOPATH=/tmp/go \
    PATH=/go/bin:$PATH \
    VIPS_DIR=/vips

ENV PKG_CONFIG_PATH=${VIPS_DIR}/lib/pkgconfig:$PKG_CONFIG_PATH

RUN apk update && apk add --no-cache openssl ca-certificates && mkdir -p ${GOPATH}/src

RUN wget -O- https://github.com/jcupitt/libvips/releases/download/v${VIPS_VERSION}/vips-${VIPS_VERSION}.tar.gz | tar xzC /tmp

RUN wget -O- https://github.com/h2non/imaginary/archive/v${IMAGINARY_VERSION}.tar.gz | tar xzC ${GOPATH}/src

# RUN echo "@latest http://dl-cdn.alpinelinux.org/alpine/3.6/community" >> /etc/apk/repositories

RUN apk update && apk upgrade && apk add --no-cache \
        build-base \
        zlib-dev libxml2-dev glib-dev gobject-introspection-dev \
        libjpeg-turbo-dev libexif-dev lcms2-dev fftw-dev giflib-dev libpng-dev \
        libwebp-dev orc-dev tiff-dev poppler-dev librsvg-dev libgsf-dev openexr-dev \
        go git glide

RUN cd /tmp/vips-${VIPS_VERSION} && \
    ./configure \
        --disable-static \
        --disable-dependency-tracking \
        --without-python \
        --prefix=${VIPS_DIR} && \
    make && \
    make install && \
    cd ${GOPATH}/src/imaginary-${IMAGINARY_VERSION} && \
    glide install && \
    go build -o $GOPATH/bin/imaginary


# RUN apk update && apk add --no-cache openssl ca-certificates && mkdir -p ${GOPATH}/src && \
#     wget -O- https://github.com/jcupitt/libvips/releases/download/v${VIPS_VERSION}/vips-${VIPS_VERSION}.tar.gz | tar xzC /tmp && \
#     wget -O- https://github.com/h2non/imaginary/archive/v${IMAGINARY_VERSION}.tar.gz | tar xzC ${GOPATH}/src && \
#     echo "@latest http://dl-cdn.alpinelinux.org/alpine/3.6/community" >> /etc/apk/repositories && \
#     apk update && apk upgrade && apk add --no-cache \
#         build-base \
#         zlib-dev libxml2-dev glib-dev gobject-introspection-dev \
#         libjpeg-turbo-dev libexif-dev lcms2-dev fftw-dev giflib-dev libpng-dev \
#         libwebp-dev orc-dev tiff-dev poppler-dev librsvg-dev libgsf-dev openexr-dev \
#         go git glide@latest && \
#     cd /tmp/vips-${VIPS_VERSION} && \
#     ./configure \
#         --disable-static \
#         --disable-dependency-tracking \
#         --without-python \
#         --prefix=${VIPS_DIR} && \
#     make && \
#     make install && \
#     cd ${GOPATH}/src/imaginary-${IMAGINARY_VERSION} && \
#     glide install && \
#     go build -o $GOPATH/bin/imaginary


FROM alpine:3.6

RUN apk update \
    apk upgrade && \
    apk add --no-cache \
        openssl ca-certificates \
        zlib libxml2 glib gobject-introspection \
        libjpeg-turbo libexif lcms2 fftw giflib libpng \
        libwebp orc tiff poppler-glib librsvg libgsf openexr && \
    rm -rf /var/cache/apk/*

COPY --from=builder /vips/lib/ /usr/local/lib
COPY --from=builder /tmp/go/bin/imaginary /usr/bin/imaginary

# Copiamos el certificado.
RUN  wget -O /usr/local/share/ca-certificates/cacert.crt https://imolko-dev.nyc3.digitaloceanspaces.com/certs/certs/ca-dev/cacert.crt \
    && update-ca-certificates

ENV PORT 9000
EXPOSE 9000

ENTRYPOINT ["/usr/bin/imaginary"]
