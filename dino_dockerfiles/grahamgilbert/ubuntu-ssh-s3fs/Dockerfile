FROM grahamgilbert/ubuntu-ssh
ENV SSH_CHROOT_DIRECTORY=/data
RUN apt-get update && apt-get install -y wget automake autotools-dev g++ git libcurl4-gnutls-dev libfuse-dev libssl-dev libxml2-dev make pkg-config && git clone https://github.com/s3fs-fuse/s3fs-fuse

WORKDIR s3fs-fuse
RUN ./autogen.sh && ./configure --prefix=/usr --with-openssl && make && make install && mkdir -p /data && chmod 777 /data
WORKDIR /
ADD run.sh /run.sh
RUN rm -rf /s3fs-fuse && chmod +x /run.sh && echo "user_allow_other" > /etc/fuse.conf
