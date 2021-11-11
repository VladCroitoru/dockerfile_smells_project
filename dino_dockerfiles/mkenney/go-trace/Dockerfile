FROM divan/golang:gotrace
ENV GOOS=linux
WORKDIR /go/src
COPY entrypoint.sh /entrypoint.sh
RUN set -x \
    && echo 'alias ll="ls -laF"' >> /root/.bashrc \
    && echo 'alias e="exit"' >> /root/.bashrc \
    && echo 'alias cls="clear"' >> /root/.bashrc \
    # dep
    && go get -u github.com/golang/dep/cmd/dep \
    # gotrace
    && mkdir -p github.com/divan \
    && cd github.com/divan \
    && git clone https://github.com/divan/gotrace.git \
    && cd gotrace \
    && git checkout go18 \
    && dep init \
    && go install \
    # entrypoint
    && chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh
