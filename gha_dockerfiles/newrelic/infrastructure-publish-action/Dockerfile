# centos-8 provides more up-to-date version of createrepo which supports rpm weak dependencies
FROM centos:8

# Args
ARG AWS_S3_MOUNT_DIRECTORY=/mnt/s3

# Tools
# validate s3fs-fuse with the sec team
RUN dnf install -y createrepo \
                    unzip \
                    bzip2 \
                    gnupg2 \
                    curl \
                    make \
                    wget

# install golang version 1.15.7
RUN curl -L https://golang.org/dl/go1.17.2.linux-amd64.tar.gz | tar xvzf - -C /usr/local
ENV PATH $PATH:/usr/local/go/bin


# Sadly installing aptly with apt lead you to a old version not supporting gpg2
WORKDIR /tmp
RUN wget -q https://github.com/aptly-dev/aptly/releases/download/v1.4.0/aptly_1.4.0_linux_amd64.tar.gz
RUN tar xzf aptly_1.4.0_linux_amd64.tar.gz
RUN mv ./aptly_1.4.0_linux_amd64/aptly /usr/bin/aptly


RUN wget -q https://github.com/kahing/goofys/releases/download/v0.24.0/goofys -O /usr/bin/goofys
RUN chmod +x /usr/bin/goofys

RUN curl -s "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip -q awscliv2.zip
RUN ./aws/install

# Prepare action
WORKDIR /home/gha/publisher
ADD publisher .
RUN go build -o /bin/publisher ./publisher.go
RUN chmod +x /bin/publisher

WORKDIR /home/gha
ADD schemas ./schemas
ADD scripts/Makefile .
ADD scripts/mount-s3.sh .
RUN chmod +x ./mount-s3.sh
RUN mkdir ./assets
RUN mkdir $AWS_S3_MOUNT_DIRECTORY
ENV AWS_S3_MOUNT_DIRECTORY $AWS_S3_MOUNT_DIRECTORY
ENV DEST_PREFIX $DEST_PREFIX

# Run action
CMD ["make", "--jobs=1"]
