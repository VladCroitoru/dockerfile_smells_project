FROM centos:centos7

RUN  yum install epel-release -y \
    && yum install bc jq pwgen python-pip python-devel gcc git libselinux-python wget vim bash-completion -y \
    && yum install https://centos7.iuscommunity.org/ius-release.rpm -y \
    && yum install python36u -y \
    && yum install openssl  -y \
    && yum install sshpass -y \
    && yum install autoconf automake libtool python-devel -y

RUN pip install --upgrade pip

RUN pip install \
    netaddr==0.7.19 \
    pycrypto==2.6.1 \
    ansible==2.5.2 \
    httpie==0.9.9 \
    git+git://github.com/apache/libcloud.git@v2.3.0 \
    google-api-python-client==1.6.5 \
    google-auth==1.4.1 \
    google-auth-httplib2==0.0.3 \
    ipaddress \
    httplib2==0.10.3 \
    ansible-modules-hashivault==3.9.4 \
    ansible-vault==1.1.1 \
    apache-libcloud==2.3.0 \
    asn1crypto==0.24.0 \
    backports.ssl-match-hostname==3.5.0.1 \
    bcrypt==3.1.4 \
    cachetools==2.1.0 \
    certifi==2018.8.13 \
    cffi==1.11.5 \
    chardet==3.0.4 \
    cryptography==2.3 \
    docker-py==1.10.6 \
    docker-pycreds==0.4.0 \
    enum34==1.1.6 \
    httpie==0.9.9 \
    hvac==0.6.3 \
    idna==2.7 \
    Jinja2==2.10 \
    MarkupSafe==1.0 \
    netaddr==0.7.19 \
    oauth2client==4.1.2 \
    paramiko==2.4.1 \
    pyasn1==0.4.4 \
    pyasn1-modules==0.2.2 \
    pycparser==2.18 \
    Pygments==2.2.0 \
    pyjq==2.3.1 \
    PyNaCl==1.2.1 \
    PyYAML==3.13 \
    requests==2.19.1 \
    rsa==3.4.2 \
    six==1.11.0 \
    uritemplate==3.0.0 \
    urllib3==1.23 \
    websocket-client==0.54.0

RUN  yum remove -y autoconf automake libtool python-devel

COPY files/kubernetes.repo /etc/yum.repos.d/kubernetes.repo
RUN  yum install -y kubectl-1.12.1
RUN  kubectl completion bash > /etc/bash_completion.d/kubectl

COPY files/google-cloud-sdk.repo /etc/yum.repos.d/google-cloud-sdk.repo
RUN  yum install -y install google-cloud-sdk

WORKDIR /tmp
RUN  wget -q https://storage.googleapis.com/kubernetes-helm/helm-v2.14.2-linux-amd64.tar.gz -O /tmp/helm-2.14.2.tar.gz \
    && tar xzf  /tmp/helm-2.14.2.tar.gz \
    && mv linux-amd64/helm /usr/local/bin/helm \
    && rm -rf /tmp/helm-2.14.2.tar.gz /tmp/linux-amd64

WORKDIR /
ADD files/init.sh .
ADD files/vimrc /root/.vimrc
ENTRYPOINT ["/init.sh"]
