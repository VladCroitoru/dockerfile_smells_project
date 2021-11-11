FROM microdc/ubuntu-testing-container
RUN mkdir /app
WORKDIR /app
COPY ./ /app/
RUN ./test.sh


FROM ubuntu:16.04
RUN apt-get update -q

#Install s3fs
RUN apt-get install -y automake \
                       autotools-dev \
                       fuse \
                       g++ \
                       libcurl4-gnutls-dev \
                       libfuse-dev \
                       libssl-dev \
                       libxml2-dev \
                       make \
                       pkg-config \
                       curl \
                       tar
RUN curl -L https://github.com/s3fs-fuse/s3fs-fuse/archive/v1.83.tar.gz | tar xvz -C /usr/src
RUN cd /usr/src/s3fs-fuse-1.83 && ./autogen.sh && ./configure --prefix=/usr && make && make install
RUN chmod -R 755 /mnt

#INSTALL SFTP
RUN apt-get update && \
    apt-get -y install openssh-server && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /var/run/sshd && \
    rm -f /etc/ssh/ssh_host_*key*
COPY sshd_config /etc/ssh/sshd_config


COPY entrypoint.sh /usr/local/bin/
RUN chmod 700 /usr/local/bin/entrypoint.sh
EXPOSE 22
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
