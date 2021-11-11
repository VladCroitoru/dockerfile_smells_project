FROM registry.gitlab.com/fdroid/ci-images-server:latest

COPY signing-key.asc /

RUN gpg --import /signing-key.asc

RUN git clone --depth 1 https://gitlab.com/fdroid/fdroidserver.git \
    && cd fdroidserver \
    && pyvenv fdroidserver-env \ 
    && . fdroidserver-env/bin/activate \ 
    && pip3 install fdroidserver 

VOLUME ["/repo"]
WORKDIR /repo

ENTRYPOINT ["/fdroidserver/fdroid"]
CMD ["--help"]
