FROM tomcat:alpine

ENV FPC_VERSION 3.0.2 
ENV FPC_ARCH x86_64-linux
ENV DB_HOST mysql_server
ENV DB_USER root
ENV DB_PASSWORD password

COPY ZeroJudge_CONSOLE /ZeroJudge_CONSOLE
COPY JudgeServer_CONSOLE /JudgeServer_CONSOLE
COPY zerojudge.sql /root
COPY docker-entrypoint.sh /usr/local/bin

RUN apk add --no-cache --virtual .native-build-deps git rsync apache-ant gcc g++ python3 mysql-client \
    && cd /tmp \
    && wget "ftp://ftp.hu.freepascal.org/pub/fpc/dist/${FPC_VERSION}/${FPC_ARCH}/fpc-${FPC_VERSION}.${FPC_ARCH}.tar" -O fpc.tar \
    && tar xf "fpc.tar" \
    && cd "fpc-${FPC_VERSION}.${FPC_ARCH}" \
    && rm demo* doc* \
    && mkdir /lib64 \
    && ln -s /lib/ld-musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 \
    && echo -e '/usr\nN\nN\nN\n' | sh ./install.sh \
    && find "/usr/lib/fpc/${FPC_VERSION}/units/${FPC_ARCH}/" -type d -mindepth 1 -maxdepth 1 \
        -not -name 'fcl-base' \
        -not -name 'rtl' \
        -not -name 'rtl-console' \
        -not -name 'rtl-objpas' \
        -exec rm -r {} \; \
    && rm -r "/lib64" "/tmp/"* /usr/local/tomcat/webapps/* \
    && chmod -R 755 /ZeroJudge_CONSOLE /JudgeServer_CONSOLE /usr/local/bin/docker-entrypoint.sh

COPY ROOT /usr/local/tomcat/webapps/ROOT
COPY ZeroJudge_Server /usr/local/tomcat/webapps/ZeroJudge_Server

EXPOSE 80
CMD ["docker-entrypoint.sh"]
