FROM stackfeed/alpine

LABEL vendor=actionml
ENV USER aml

ADD requirements.txt /tmp

RUN cd /tmp && \
    apk add --no-cache --virtual .build-deps \
        build-base \
        python3-dev \
        libffi-dev \
        openssl-dev \
      && \
    apk add --no-cache \
          git \
          openssh-client \
          less \
          groff \
          python3 \
          libffi \
          libssl1.0 \
      && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install -r requirements.txt && \
    ln -s /config/.aws /root/.aws && \
      \
    curl -sSLo /usr/bin/consult https://github.com/outbrain/consult/releases/download/v0.0.9/consult-linux-amd64 && \
    chmod 755 /usr/bin/consult && \
      \
    useradd -Um -d /home/$USER $USER && passwd -d $USER && \
    apk del --no-cache .build-deps && \
    rm -rf /tmp/* 

# Expose data volumes
WORKDIR "/config"
VOLUME ["/config", "/apps", "/ssh"]

ADD entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
