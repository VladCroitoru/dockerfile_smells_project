FROM ubuntu:12.04
ARG PIP_INDEX_URL
ARG PIP_TRUSTED_HOST
ARG APT_PROXY
ONBUILD ENV PIP_TRUSTED_HOST=$PIP_TRUSTED_HOST PIP_INDEX_URL=$PIP_INDEX_URL
ONBUILD RUN test -n $APT_PROXY && echo 'Acquire::http::Proxy \"$APT_PROXY\";' >/etc/apt/apt.conf.d/proxy

RUN sed 's/main$/main universe/' -i /etc/apt/sources.list && \
    apt-get update -qq && \
    apt-get install -qy \
        netbase ca-certificates apt-transport-https \
        build-essential python python-dev \
        libxml2-dev libssl-dev libxslt1-dev \
        libmysqlclient-dev \
        libpq-dev \
        libevent-dev \
        libffi-dev libssl-dev \
        libpcre3-dev libz-dev \
        libjpeg8-dev \
        libblas-dev liblapack-dev libatlas-base-dev gfortran \
        unixodbc unixodbc-dev \
        ghostscript \
        telnet vim htop strace ltrace iputils-ping curl wget lsof git libdb4.8-dev sudo \
        && \
    rm -rf /var/lib/apt/lists

# en_US.UTF-8 is needed for python to consider stdin/stdout as utf8
# other are custom to provide backward support with scrapy cloud 1.0
RUN locale-gen en_US.UTF-8 de_DE.UTF-8 nl_NL.UTF-8 fr_FR.UTF-8
# TERM needs to be set here for exec environments
# LANG for locale
# PIP_TIMEOUT so installation doesn't hang forever
# PYTHONWARNINGS https://urllib3.readthedocs.org/en/latest/security.html#disabling-warnings
ENV TERM=xterm \
    LANG=en_US.UTF-8 \
    PIP_TIMEOUT=180 \
    PYTHONWARNINGS="ignore:A true SSLContext object is not available"

ADD https://bootstrap.pypa.io/get-pip.py /get-pip.py
# pinned setuptools as a work-around for https://github.com/pypa/setuptools/issues/951
RUN python /get-pip.py && pip install -U pip==8.1.2 setuptools==33.1.1
COPY requirements-base-pre.txt /
RUN pip install --no-cache-dir -r requirements-base-pre.txt
COPY requirements-base.txt /
RUN pip install --no-cache-dir -r requirements-base.txt
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /app
COPY addons_eggs /app/addons_eggs
RUN chown nobody:nogroup -R /app/addons_eggs

ADD eggbased-entrypoint /usr/local/sbin/
RUN chmod +x /usr/local/sbin/eggbased-entrypoint && \
    ln -s /usr/local/sbin/eggbased-entrypoint /usr/local/sbin/start-crawl
