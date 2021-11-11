FROM criticalblue/android

# == Install required tools

ENV NODE_VERSION 6.11.0
RUN cd && \
        wget -q https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz && \
        tar -xf node-v${NODE_VERSION}-linux-x64.tar.xz && \
        mv node-v${NODE_VERSION}-linux-x64 /opt/node && \
        rm node-v${NODE_VERSION}-linux-x64.tar.xz
ENV PATH ${PATH}:/opt/node/bin
