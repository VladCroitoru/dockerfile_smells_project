FROM nginx:alpine

LABEL Maintainers="Steve.Taylor <steve.taylor@cu.edu>"

COPY run_nginx.sh /usr/local/bin

RUN echo "http://dl-cdn.alpinelinux.org/alpine/v3.7/main" >> /etc/apk/repositories && \
    apk add busybox --update && \
    apk update && apk upgrade --no-cache --update && \
    apk add --no-cache bash && \
    apk add --no-cache python3 && \
    apk add --no-cache python3-dev && \
    apk add --no-cache dpkg && \
    update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 10 && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3 10 && \
    \
    \
    echo "Install Sphinx-docs" && \
    pip install pip --upgrade --no-cache-dir && \
    pip install Sphinx --no-cache-dir && \
    pip install sphinx_rtd_theme --no-cache-dir && \
    pip install alabaster --no-cache-dir && \
    pip install sphinx_bootstrap_theme --no-cache-dir && \
    pip install plantweb --no-cache-dir && \
    \
    \
    chmod u+x /usr/local/bin/run_nginx.sh

WORKDIR /docs

EXPOSE 80

ONBUILD COPY . /docs

ONBUILD RUN sphinx-build /docs /usr/share/nginx/html

ENTRYPOINT /usr/local/bin/run_nginx.sh
