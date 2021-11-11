FROM ubuntu:latest

# 定义构建时元数据
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL maintainer="moore@moorehy.com" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="RoyalBitcoin-Explorer" \
      org.label-schema.description="纯真比特币的区块链浏览器" \
      org.label-schema.url="https://hub.docker.com/r/littlemo/RoyalBitcoin-Explorer/" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/NewEconomicTeam/RoyalBitcoin-Explorer" \
      org.label-schema.vendor="NewEconomicTeam" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

# 替换为中科大软件源
RUN sed -i 's|archive.ubuntu.com|mirrors.ustc.edu.cn|g' /etc/apt/sources.list && \
    sed -i 's|security.ubuntu.com|mirrors.ustc.edu.cn|g' /etc/apt/sources.list

# 安装依赖库&扩展
ADD https://deb.nodesource.com/setup_8.x /tmp/setup_8.x
RUN bash /tmp/setup_8.x \
    && rm /tmp/setup_8.x \
    && apt-get install -y \
        libboost-dev libboost-all-dev \
        libdb-dev libdb++-dev libminiupnpc-dev \
        libcrypto++-dev libevent-dev \
        build-essential nodejs libzmq3-dev \
        --no-install-recommends \
    && ldconfig \
    && rm -rf /var/lib/apt/lists/*

# 设置全局环境变量
ENV WORK_DIR=/app/bitcore

# 创建路径
RUN mkdir -p ${WORK_DIR}

# 安装bitcore，并创建节点
WORKDIR /app/bitcore

RUN npm --registry https://registry.npm.taobao.org install -g --unsafe-perm=true bitcore
RUN bitcore create rbtc_node && \
    cd ${WORK_DIR}/rbtc_node && \
    bitcore install insight-api insight-ui

WORKDIR /app/bitcore/rbtc_node

RUN rm -rf ./node_modules/bitcore-node/node_modules/bitcore-lib && \
    rm -rf ./node_modules/bitcore-message/node_modules/bitcore-lib && \
    rm -rf ./node_modules/insight-api/node_modules/bitcore-lib

# 配置bitcore
COPY ./source/config/networks.js ./node_modules/bitcore-lib/lib/networks.js

# 替换insight-api资源
COPY ./source/insight-api/lib/blocks.js ./node_modules/insight-api/lib/blocks.js

# 替换insight-ui资源
COPY ./source/insight-ui/public/js/main.* \
     ./node_modules/insight-ui/public/js/
COPY ./source/insight-ui/public/views/includes/currency.html \
     ./source/insight-ui/public/views/includes/header.html \
     ./node_modules/insight-ui/public/views/includes/
COPY ./source/insight-ui/public/views/index.html \
     ./source/insight-ui/public/views/status.html \
     ./node_modules/insight-ui/public/views/
COPY ./source/insight-ui/public/index.html \
     ./node_modules/insight-ui/public/

# 设置挂载点
VOLUME [ \
    "/app", \
]

# 设置开放端口
EXPOSE 80 443

# 启动命令
CMD [ \
    "bitcored" \
]
