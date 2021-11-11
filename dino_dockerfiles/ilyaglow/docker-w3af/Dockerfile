# Made based on original version:
# https://github.com/andresriancho/w3af/blob/master/extras/docker/Dockerfile
#
# It does NOT include gtk packages for gui version
FROM ubuntu:latest

# Install basic requirements, python-lxml because it doesn't compile correctly from pip
RUN apt-get update && apt-get install -y \
  build-essential \
  ca-certificates \
  git \
  libffi-dev \
  libsqlite3-dev \
  libssl-dev \
  libxml2-dev \
  libxslt1-dev \
  libyaml-dev \
  python-dev \
  python-lxml \
  python-pip \
&& rm -rf /var/lib/apt/lists/*

# Get and install pip
RUN pip install --upgrade pip \
# Pypi dependencies
  && pip install \
    chardet==2.1.1 \
    clamd==1.0.1 \
    cluster==1.1.1b3 \
    darts.util.lru==0.5 \
    esmre==0.3.1 \
    Flask==0.10.1 \
    futures==2.1.5 \
    GitPython==0.3.2.RC1 \
    guess-language==0.2 \
    halberd==0.2.4 \
    Jinja2==2.7.3 \
    lxml==3.4.4 \
    markdown==2.6.1 \
    mitmproxy==0.13 \
    msgpack-python==0.4.4 \
    ndg-httpsclient==0.3.3 \
    nltk==3.0.1 \
    pdfminer==20140328 \
    phply==0.9.1 \
    psutil==2.2.1 \
    pyasn1==0.1.9 \
    pybloomfiltermmap==0.3.14 \
    pyclamd==0.3.15 \
    PyGithub==1.21.0 \
    pyOpenSSL==0.15.1 \
    python-ntlm==1.0.1 \
    PyYAML==3.12 \
    ruamel.ordereddict==0.4.8 \
    scapy-real==2.2.0-dev \
    tblib==0.2.0 \
    termcolor \
    tldextract==1.7.2 \
    vulndb==0.0.19 \
  && rm -rf /root/.cache/pip \
  && apt-get purge -y build-essential

# Add the w3af user with home folder
RUN useradd w3af -m

# Clone w3af from official repo
RUN git clone --depth=1 \
              --branch=master \
              https://github.com/andresriancho/w3af.git /home/w3af/w3af \
  && rm -rf /home/w3af/w3af/.git \
  && apt autoremove -y \
  && chown -R w3af /home/w3af/w3af

# Prepare the startup
USER w3af
WORKDIR /home/w3af/w3af

# You can comment out runtime check for dependencies if w3af complaining about it
# The approach of checking exact versions of packages feels wrong tbh
# RUN sed 's/    dependency_check()/    # dependency_check()/g' -i /home/w3af/w3af/w3af_api
# RUN sed 's/dependency_check()/# dependency_check()/g' -i /home/w3af/w3af/w3af_console
