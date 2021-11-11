FROM debian:latest

ENV PYTHON_VER 3.6.4
ENV TWISTED_VER 16.2.0
ENV APP_LOCATION /opt/otree
ENV LAUNCHER start_app
ENV INIT_SCRIPT entrypoint

EXPOSE 8000
CMD ["${LAUNCHER}"]
ENTRYPOINT ["${INIT_SCRIPT}"]

COPY . ${APP_LOCATION}

RUN mkdir -p ${APP_LOCATION} && ln -s ${APP_LOCATION}/${LAUNCHER} /usr/local/bin/${LAUNCHER} && \
    ln -s ${APP_LOCATION}/${INIT_SCRIPT} /usr/local/bin/${INIT_SCRIPT} && \
    chmod +x ${APP_LOCATION}/${LAUNCHER} && \
    chmod +x ${APP_LOCATION}/${INIT_SCRIPT} && \
    apt-get update && \
    apt-get install -y --no-install-recommends build-essential make wget libssl-dev zlib1g-dev libsqlite3-dev ca-certificates && \
    wget https://www.python.org/ftp/python/${PYTHON_VER}/Python-${PYTHON_VER}.tar.xz && \
    tar -xvf Python-${PYTHON_VER}.tar.xz && cd Python-${PYTHON_VER} && \
    ./configure --with-lto --enable-optimizations --enable-loadable-sqlite-extensions && make -j$(nproc) && make install && \
    cd - && rm -rf Python* && \
    wget https://pypi.python.org/packages/18/85/eb7af503356e933061bf1220033c3a85bad0dbc5035dfd9a97f1e900dfcb/Twisted-${TWISTED_VER}.tar.bz2#md5=8b35a88d5f1a4bfd762a008968fddabf && \
    tar -xvf Twisted-${TWISTED_VER}.tar.bz2 && cd Twisted-${TWISTED_VER} && python3 setup3.py install && \
    cd - && rm -rf Twisted* && \
    cd ${APP_LOCATION} && \
    pip3 install --no-cache-dir -U pip && \
    pip3 install --no-cache-dir -U otree && \
    pip3 install --no-cache-dir -r requirements_base.txt && \
    cd - && \
    apt-get remove --purge -y build-essential make wget libssl-dev zlib1g-dev libsqlite3-dev ca-certificates $(apt-mark showauto) && \
    rm -rf /var/lib/apt/apt/lists/*
