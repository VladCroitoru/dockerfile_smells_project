FROM php:7.1
COPY fs /
RUN cd /tmp && \
    curl https://github.com/swoole/swoole-src/archive/v1.9.22.tar.gz \
        -o swoole-src-1.9.22.tgz -L && \
    tar xpf swoole-src-1.9.22.tgz && \
    cd /tmp/swoole-src-1.9.22 && \
    phpize && ./configure && make -j$(nproc) && make install
WORKDIR /root
CMD bash
