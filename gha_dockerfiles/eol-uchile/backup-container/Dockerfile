FROM ubuntu:18.04

RUN apt-get update && apt-get install -y apt-transport-https wget lsb-release gnupg && \
  echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.0.list && \
  wget -qO - https://www.mongodb.org/static/pgp/server-4.0.asc | apt-key add - && \
  wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
  echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" >> /etc/apt/sources.list.d/postgresql.list && \
  apt-get update && \
  apt-get install -y \
    mongodb-org-tools \
    postgresql-client-12 \
    mysql-client \
    nmap \
    unzip && \
  rm -rf /var/lib/apt/lists/*

RUN wget https://downloads.rclone.org/v1.53.1/rclone-v1.53.1-linux-amd64.zip && \
  unzip rclone-v1.53.1-linux-amd64.zip && \
  cp rclone-v1.53.1-linux-amd64/rclone /usr/bin/rclone && \
  chmod 755 /usr/bin/rclone && \
  rm -rf rclone-v1.53.1-linux-amd64

RUN wget https://dl.min.io/server/minio/release/linux-amd64/archive/minio_20210607214051.0.0_amd64.deb && \
  dpkg -i minio_20210607214051.0.0_amd64.deb

# Keys for minio, which is NOT exposed to the internet
ENV MINIO_ROOT_USER minio
ENV MINIO_ROOT_PASSWORD localminiosecret

# Platform name
ENV PLATFORM_NAME ""

# Postgresql server
ENV PLATFORM_POSTGRESQL_HOST ""
ENV PLATFORM_POSTGRESQL_PORT ""
ENV PLATFORM_POSTGRESQL_USER ""
ENV PGPASSWORD ""
ENV PLATFORM_POSTGRESQL_DATABASES "edxapp edxapp_csmh"

# MySQL server
ENV PLATFORM_MYSQL_HOST ""
ENV PLATFORM_MYSQL_USER ""
ENV PLATFORM_MYSQL_PASSWORD ""
ENV PLATFORM_MYSQL_DATABASES "edxapp edxapp_csmh"

# MongoDB server
ENV PLATFORM_MONGODB_HOST ""
ENV PLATFORM_MONGODB_USER ""
ENV PLATFORM_MONGODB_PASSWORD ""

# S3 Server
ENV PLATFORM_S3_URL ""
ENV PLATFORM_S3_ACCESS_KEY ""
ENV PLATFORM_S3_SECRET_KEY ""
ENV PLATFORM_S3_BUCKETS ""

# GDrive
ENV PLATFORM_GRIVE_CLIENT_ID ""
ENV PLATFORM_GDRIVE_CLIENT_SECRET ""
ENV PLATFORM_GDRIVE_SCOPE ""
ENV PLATFORM_GDRIVE_TOKEN ""

# NAS
ENV NAS_HOST ""
ENV NAS_USER ""
ENV NAS_PASS ""
ENV NAS_KEY_FILE_PASS  ""

# HOST FS
ENV HOST_MOUNT "/host_mount"

RUN mkdir -p /root/.config/rclone

ADD scripts /root/scripts
