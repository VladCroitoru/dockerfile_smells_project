FROM golang:1.15-buster as golang
RUN go get github.com/spelufo/on-change && \
    go get github.com/sugyan/ttyrec2gif

FROM debian:buster-slim
COPY --from=golang /go/bin/on-change /go/bin/ttyrec2gif /usr/local/bin/
# hadolint ignore=DL3008
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ca-certificates \
        fonts-font-awesome \
        fonts-linex \
        fonts-noto-extra \
        fonts-sil-ezra \
        ghostscript \
        graphicsmagick \
        gosu \
        graphviz \
        groff \
        librsvg2-bin \
        lmodern \
        make \
        netbase \
        pandoc \
        texlive-extra-utils \
        texlive-fonts-extra \
        texlive-fonts-recommended \
        texlive-font-utils \
        texlive-lang-arabic \
        texlive-lang-other \
        texlive-latex-base \
        texlive-latex-extra \
        texlive-luatex \
        texlive-publishers \
        texlive-xetex \
        qpdf \
    && \
    rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /var/cache/apt/archives/*
ADD [ "https://www.shore.co.il/blog/static/runas", "/entrypoint" ]
ENTRYPOINT [ "/bin/sh", "/entrypoint" ]
CMD [ "on-change", ".", "make" ]
VOLUME /volume
WORKDIR /volume
ENV HOME /volume
# Run a test build.
COPY example/ /example/
RUN make --debug=j --keep-going -C /example test
