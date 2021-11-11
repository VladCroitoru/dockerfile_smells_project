FROM ubuntu:16.10
MAINTAINER Karl Hepworth

RUN sed -i.bak -r 's/(archive|security).ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

# Install dependencies.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       software-properties-common curl \
       python-setuptools init unzip \
       rsync rsyslog systemd sudo
RUN sed -i 's/^\($ModLoad imklog\)/#\1/' /etc/rsyslog.conf
#ADD etc/rsyslog.d/50-default.conf /etc/rsyslog.d/50-default.conf

# Install PIP.
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" \
    && python get-pip.py

# Install xz-utils
# Dependent package is not found by apt-get
# URL referes to non-existant file - so we'll
# install a very similar one we know works.
RUN apt-get install -y gdebi-core && \
    curl -O http://old-releases.ubuntu.com/ubuntu/pool/main/x/xz-utils/xz-utils_5.1.1alpha+20120614-2ubuntu1_amd64.deb && \
    gdebi -n ./xz-utils_5.1.1alpha+20120614-2ubuntu1_amd64.deb && \
    rm -f ./xz-utils_5.1.1alpha+20120614-2ubuntu1_amd64.deb

# Install Ansible
RUN pip install urllib3 pyOpenSSL ndg-httpsclient pyasn1 ansible cryptography

RUN rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

COPY initctl_faker .
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker /sbin/initctl

# Make directory /etc/ansible
RUN mkdir /etc/ansible

# Install Ansible inventory file
RUN echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts

# Report some information
RUN python --version
RUN ansible --version