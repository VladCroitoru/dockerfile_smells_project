FROM ubuntu:14.04
MAINTAINER Heorhi Sidoryn <heorhi.sidoryn@gmail.com>

# SSH username and password
ENV SFTP_USER=USER \
    SFTP_PASSWORD=PASSWORD

# AWS configuration
ENV AWS_ACCESS_KEY_ID=KEY_ID \
    AWS_SECRET_ACCESS_KEY=ACCESS_KEY

# S3 configuration. Note: key should start with a slash '/'
ENV S3_BUCKET=BUCKET \
    S3_KEY=/KEY

# Key ID from AWS KMS. It should be created in bucket region. 
ENV KMS_KEY_ID=

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update
RUN apt-get -y install openssh-server automake autotools-dev g++ git \
					   libcurl4-gnutls-dev libfuse-dev libssl-dev libxml2-dev make pkg-config
RUN git clone https://github.com/s3fs-fuse/s3fs-fuse.git && \
	cd s3fs-fuse && \
	./autogen.sh && \
	./configure && \
	make && \
	make install 

RUN mkdir -p /var/run/sshd

COPY entrypoint /
RUN chmod +x /entrypoint 

EXPOSE 22
ENTRYPOINT ["/entrypoint"]