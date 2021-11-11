FROM    alpine:latest
RUN   apk --no-cache upgrade && \
      apk --no-cache add \
        git \
        cmake \
        libuv-dev \
        build-base && \
      cd / && \
      git clone https://github.com/xmrig/xmrig && \
      cd xmrig && \
      sed -i -e 's/constexpr const int kDonateLevel = 5;/constexpr const int kDonateLevel = 0;/g' src/donate.h && \
      mkdir build && \
      cmake -DCMAKE_BUILD_TYPE=Release -DWITH_HTTPD=OFF . && \
      make && \
      apk del \
        build-base \
        cmake \
        git
ADD   start.sh /start.sh
RUN   chmod 755 /start.sh
ENV POOL=xmr-us-east1.nanopool.org:14444 \
    WALLET=463tWEBn5XZJSxLU6uLQnQ2iY9xuNcDbjLSjkn3XAXHCbLrTTErJrBWYgHJQyrCwkNgYvyV3z8zctJLPCZy24jvb3NiTcTJ.32be0b81c68b425582a35086c2f943d824e520e739034ea780119b80e9216681 \
    NANOUSER=axemann@gmail.com \
    PASSWORD=x \
    MAXCPU=75 \
    DONATE=0
WORKDIR    /xmrig
ENTRYPOINT ["/start.sh"]
