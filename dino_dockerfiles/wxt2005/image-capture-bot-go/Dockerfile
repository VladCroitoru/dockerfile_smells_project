FROM ubuntu:focal

ARG VIPS_VERSION=8.10.2
ARG GO_VERSION=1.15.5

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update \
    && apt-get install -y wget
RUN apt-get update \
    && apt-get install -y \
    wget build-essential pkg-config glib2.0-dev libexpat1-dev \
    libtiff5-dev libjpeg-turbo8-dev libgsf-1-dev libpng-dev libwebp-dev \
    && wget -O- https://github.com/libvips/libvips/releases/download/v${VIPS_VERSION}/vips-${VIPS_VERSION}.tar.gz | tar xzC /tmp \
    && cd /tmp/vips-${VIPS_VERSION} \
    && ./configure \
    && make && make install && ldconfig \
    && rm -rf /tmp/vips-${VIPS_VERSION}
RUN wget https://golang.org/dl/go${GO_VERSION}.linux-amd64.tar.gz && tar -C /usr/local -xzf go${GO_VERSION}.linux-amd64.tar.gz
ENV PATH $PATH:/usr/local/go/bin

RUN mkdir -p /go/image-capture-bot-go
WORKDIR /go/image-capture-bot-go
COPY . .

RUN go build -o app .

CMD ["./app"]
