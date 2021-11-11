FROM centos
RUN yum install -y openssl git wget
RUN wget https://storage.googleapis.com/golang/go1.9.2.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go1.9.2.linux-amd64.tar.gz
ENV PATH="/usr/local/go/bin:${PATH}"
