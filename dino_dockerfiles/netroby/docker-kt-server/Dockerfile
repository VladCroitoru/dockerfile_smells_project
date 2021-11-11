FROM alpine
RUN apk add -U curl ; \
        curl -L -O https://github.com/xtaci/kcptun/releases/download/v20160922/kcptun-linux-amd64-20160922.tar.gz; \
        tar zxvf kcptun-linux-amd64-20160922.tar.gz; \
        rm *.gz; \
        rm client*; \
        mv server_linux_amd64 /bin/server; \
        apk del curl ; 
CMD ["server"]
