FROM golang:1.10.3

LABEL maintainer="Paul Otto <paul.otto@ticketmaster.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
            git \
            curl \
            unzip \
    && rm -rf /var/lib/apt/lists/*

# ENV for Dep
ENV GODEP_VERSION v0.5.0
ENV GODEP_URL https://github.com/golang/dep/releases/download/$GODEP_VERSION/dep-linux-amd64
ENV GODEP_DOWNLOAD_SHA256 287b08291e14f1fae8ba44374b26a2b12eb941af3497ed0ca649253e21ba2f83
# ENV for Glide
ENV GLIDE_VERSION v0.13.1
ENV GLIDE_DOWNLOAD_URL https://github.com/Masterminds/glide/releases/download/$GLIDE_VERSION/glide-$GLIDE_VERSION-linux-amd64.tar.gz
ENV GLIDE_DOWNLOAD_SHA256 c403933503ea40308ecfadcff581ff0dc3190c57958808bb9eed016f13f6f32c
ENV PATH $PATH:/usr/local/glide/linux-amd64

RUN curl -fsSL "$GLIDE_DOWNLOAD_URL" -o glide.tar.gz \
    && echo "$GLIDE_DOWNLOAD_SHA256  glide.tar.gz" | sha256sum -c - \
    && mkdir -p /usr/local/glide \
    && tar -C /usr/local/glide -xzf glide.tar.gz \
    && rm glide.tar.gz \
    && curl -fsSL "$GODEP_URL" -o dep \
    && echo "$GODEP_DOWNLOAD_SHA256 dep" | sha256sum -c - \
    && chmod +x dep \
    && mv dep /usr/local/bin \
    && go get -u github.com/Masterminds/glide-report \
    && go get -u github.com/sgotti/glide-vc \
    && go get -u github.com/ngdinhtoan/glide-cleanup \
    && go get -u gopkg.in/alecthomas/gometalinter.v2 \
    && go get -u github.com/kisielk/errcheck \
    && go get -u github.com/mitchellh/gox \
    && go get -u github.com/smartystreets/goconvey \
    && go get -u github.com/golang/lint/golint \
    && go get -u honnef.co/go/tools/cmd/gosimple \
    && go get -u github.com/mdempsky/unconvert \
    && go get -u github.com/opennota/check/cmd/structcheck \
    && go get -u github.com/opennota/check/cmd/varcheck \
    && go get -u github.com/HewlettPackard/gas
