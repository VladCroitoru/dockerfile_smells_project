FROM jordan/rundeck

RUN apt-get -qq update && \
    apt-get -qqy install \
        libffi-dev libssl-dev python-dev python-pip uuid-runtime

RUN pip install --upgrade distribute && \
    pip install --upgrade cffi && \
    pip install --upgrade pyasn1 && \
    pip install cryptography && \
    pip install docker-py jinja2 markupsafe paramiko pyyaml ansible 
