FROM debian:jessie

# Stolen from python2.7-slim, so any changes can be pulled from the dif from there
# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

# runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
		ca-certificates \
		libgdbm3 \
		libsqlite3-0 \
		libssl1.0.0 \
		python-setuptools python-dev \
        build-essential wget

ADD virenv /tmp

RUN tar -xzvpf /tmp/virtualenv-15.0.0.tar.gz -C /tmp && \
    python /tmp/virtualenv-15.0.0/virtualenv.py /opt/v && \
    rm -rf /tmp/virtualenv-15.0.0

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    zip

RUN /usr/bin/easy_install virtualenv
RUN virtualenv /opt/v

RUN /opt/v/bin/pip install pyyaml


CMD ["/bin/bash"]
