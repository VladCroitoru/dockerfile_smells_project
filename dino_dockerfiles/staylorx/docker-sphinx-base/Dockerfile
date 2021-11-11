FROM oraclelinux:7-slim

LABEL Maintainers="Steve.Taylor <steve.taylor@cu.edu>"

RUN echo "Install epel-release and update" && \
    yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    yum -y update && \
    yum -y install nginx vi vim && \
    \
    \
    echo "Install Sphinx-docs" && \
    yum -y install python-pip && \
    pip install --upgrade pip && \
    pip install Sphinx --no-cache-dir && \
    pip install sphinx_rtd_theme --no-cache-dir && \
    pip install alabaster --no-cache-dir && \
    pip install sphinx_bootstrap_theme --no-cache-dir && \
    pip install plantweb --no-cache-dir && \
    \
    \
    echo "=> Cleanup!" && \
    yum -y remove epel-release && \
    yum -y -q clean all && \
    rm -rf /var/cache/yum 

WORKDIR /docs

EXPOSE 80

ONBUILD COPY . /docs

ONBUILD RUN sphinx-build /docs /usr/share/nginx/html

ENTRYPOINT /usr/sbin/nginx -g 'daemon off;'

