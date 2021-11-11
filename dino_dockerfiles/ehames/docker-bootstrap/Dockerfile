FROM alpine:edge

ARG compose_version=1.8.0

RUN apk --no-cache add python py2-pip git &&\
    git clone --branch ${compose_version} https://github.com/docker/compose.git /code/compose &&\
    cd /code/compose &&\
    pip --no-cache-dir install -r requirements.txt -r requirements-dev.txt pyinstaller==3.1.1 &&\
    git rev-parse --short HEAD > compose/GITSHA &&\
    ln -s /lib /lib64 && ln -s /lib/libc.musl-x86_64.so.1 ldd && ln -s /lib/ld-musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 && \
    pyinstaller docker-compose.spec &&\
    unlink /lib/ld-linux-x86-64.so.2 /lib64 ldd ||true &&\
    mv dist/docker-compose /usr/local/bin/docker-compose &&\
    pip freeze | xargs pip uninstall -y &&\
    apk del python py-pip git &&\
    rm -rf /code /usr/lib/python2.7/ /root/.cache /var/cache/apk/* &&\
    chmod +x /usr/local/bin/docker-compose

ENTRYPOINT ["/usr/local/bin/docker-compose"]
