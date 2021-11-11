FROM centos:6

RUN yum groupinstall -y "Development tools"

# Dependancies for downloading and compilling Python
RUN yum install -y \
    tar \
    curl \
    python-devel \
    zlib-devel \
    bzip2-devel \
    openssl-devel \
    ncurses-devel \
    sqlite-devel \
    readline-devel \
    tk-devel \
    gdbm-devel \
    db4-devel \
    libpcap-devel \
    xz-devel

# Dependancies for compilling DB clients
RUN yum install -y \
    mysql-devel \
    postgresql-devel

# Dependancies for compilling Pillow
RUN yum install -y \
    zlib-devel \
    libjpeg-turbo-devel \
    libtiff-devel \
    freetype-devel

# Dependancies for instaling lxml
RUN yum install -y \
    libxslt-devel \
    libxml2-devel

COPY build-python.sh /usr/local/bin/build-python.sh
COPY get-pip.py /usr/local/bin/get-pip.py
RUN chmod 755 /usr/local/bin/build-python.sh

ENTRYPOINT ["/usr/local/bin/build-python.sh"]
