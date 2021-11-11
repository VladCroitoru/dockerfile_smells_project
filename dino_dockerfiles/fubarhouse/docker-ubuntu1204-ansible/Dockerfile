FROM geerlingguy/docker-ubuntu1204-ansible
MAINTAINER Karl Hepworth

# Install our dependencies
RUN apt-get update && \
    apt-get install -y wget gcc make python-pip

# Upgrade python to 2.7.13
RUN wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz \
    && tar zxf ./Python-2.7.13.tgz \
    && cd Python-2.7.13 \
    && ./configure \
    && make \
    && make install \
    && rm -f ../Python-2.7.13.tgz

RUN pip install -i https://pypi.python.org/simple/ --upgrade pip

# Install Ansible
RUN apt-get remove -y ansible
RUN pip install urllib3 pyOpenSSL ndg-httpsclient pyasn1 cryptography
RUN pip install virtualenv virtualenvwrapper
RUN pip install ansible

# General cleanup.
RUN rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

# Verify important installations with stdout.
RUN python --version
RUN ansible --version