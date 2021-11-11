FROM gcc:7

COPY . /usr/src/OpenOrd
RUN cp /usr/src/OpenOrd/src/Configuration.gnu /usr/src/OpenOrd/Configuration.mk && \
    cd /usr/src/OpenOrd/src && \
    make && \
    for i in `ls /usr/src/OpenOrd/bin`; do \
        ln -s /usr/src/OpenOrd/bin/$i /usr/local/bin/$i; \
    done

RUN groupadd --gid 1000 openord && \
    useradd --uid 1000 --gid openord --shell /bin/bash --create-home openord
WORKDIR /home/openord
USER openord

CMD [ "bash" ]
