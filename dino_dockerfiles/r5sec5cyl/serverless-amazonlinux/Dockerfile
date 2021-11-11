FROM amazonlinux:1
RUN yum update -y && \
    curl --silent --location https://rpm.nodesource.com/setup_8.x | bash && \
    yum install -y python36-pip python36-setuptools unzip git nodejs
RUN pip-3.6 install --upgrade pip
RUN pip3 install --upgrade awscli && \
    npm install -g serverless

RUN yum install -y gcc openssl-devel bzip2-devel libffi-devel wget && \
    cd /usr/src && \
    wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz && \
    tar xzf Python-3.7.2.tgz && \
    ./Python-3.7.2/configure --enable-optimizations && \
    make altinstall && \
    rm /usr/bin/python && \
    rm /usr/bin/python3 && \
    ln -s /usr/src/Python-3.7.2/python /usr/bin/python && \
    ln -s /usr/src/Python-3.7.2/python /usr/bin/python3 && \
    ln -s /usr/src/Python-3.7.2/python /usr/bin/python37 && \
    ln -s /usr/src/Python-3.7.2/python /usr/bin/python3.7 && \
    rm /usr/src/Python-3.7.2.tgz

CMD /bin/bash
