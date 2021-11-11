FROM mhart/alpine-node:latest

ENV YARN_VER=v0.22.0
ENV YARN_PKG_URL=https://github.com/yarnpkg/yarn/releases/download/${YARN_VER}/yarn-${YARN_VER}.tar.gz
ENV YARN_ASC_URL=${YARN_PKG_URL}.asc
ENV YARN_PKG_FILE=/tmp/yarn-${YARN_VER}.tar.gz
ENV YARN_ASC_FILE=/tmp/yarn-${YARN_VER}.tar.gz.asc

WORKDIR "/opt"
RUN apk add --no-cache curl gnupg && \
    gpg  --keyserver ha.pool.sks-keyservers.net --recv-keys 9D41F3C3 && \
    curl -o ${YARN_PKG_FILE} -sSL ${YARN_PKG_URL} && \
    curl -o ${YARN_ASC_FILE} -sSL ${YARN_ASC_URL} && \
    gpg --verify "${YARN_ASC_FILE}" ${YARN_PKG_FILE} && \
    tar xzf ${YARN_PKG_FILE} && \
    mv /opt/dist /opt/yarn && \
    ln -sf /opt/yarn/bin/yarn /bin/yarn && \
    rm -rf /root/.gnupg ${YARN_PKG_FILE} ${YARN_ASC_FILE} \
    /opt/yarn/end_to_end_tests && \
    apk del --no-cache curl gnupg && \
    mkdir /app
WORKDIR "/app"

CMD ["yarn", "start"]
