FROM ubuntu:16.04

RUN sed -i s@archive.ubuntu.com@mirrors.aliyun.com@g /etc/apt/sources.list &&\
    apt-get update &&\

    # 安装依赖库
    apt-get install -y curl xz-utils libpng-dev vim &&\

    # cleanup
    rm -rf /var/lib/apt/lists/*

# 安装nodejs
ENV NODE_VERSION=6.9.4 \
    BOWER_VERSION=1.7.9

COPY ./node/node-v${NODE_VERSION}-linux-x64.tar.xz /
RUN tar -xJf "node-v${NODE_VERSION}-linux-x64.tar.xz" -C /usr/local --strip-components=1 &&\
    rm /node-v${NODE_VERSION}-linux-x64.tar.xz &&\
    ln -s /usr/local/bin/node /usr/local/bin/nodejs &&\
    node -v && npm -v && \

    # 安装bower
    npm -g install bower@${BOWER_VERSION} svgo


# 入口命令
ENTRYPOINT ["/bin/bash"]