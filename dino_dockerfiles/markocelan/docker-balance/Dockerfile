FROM gcc AS build
ENV BALANCE_VERSION 3.57
RUN cd /usr/src && \
    wget https://www.inlab.net/wp-content/uploads/2018/05/balance-${BALANCE_VERSION}.tar.gz ${BALANCE_VERSION}.tar.gz -O - | tar -xz && \
    cd balance-${BALANCE_VERSION} && \
    sed -i 's|^\(CFLAGS=.*\)|\1 -static|' Makefile && \
    make clean && make && \
    mv balance /bin/



FROM scratch
LABEL maintainer="marko.celan@gmail.com"
COPY --from=build /bin/balance /bin/balance

ENTRYPOINT [ "/bin/balance" ]
