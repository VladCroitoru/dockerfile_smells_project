FROM       alpine:3.6
MAINTAINER Carlos Avila "cavila@mandelbrew.com"

# Prep environment
ENV        POSTGRES_DB='' \
           POSTGRES_HOST='' \
           POSTGRES_PORT='' \
           POSTGRES_USER='' \
           POSTGRES_PASSWORD='' \
           POSTGRES_EXTRA_OPTS='--format=c' \
           POSTGRES_AWS_ACCESS_KEY_ID='' \
           POSTGRES_AWS_SECRET_ACCESS_KEY='' \
           POSTGRES_AWS_S3_BUCKET='' \
           POSTGRES_AWS_DEFAULT_REGION='' \
           POSTGRES_AWS_S3_PATH='' \
           POSTGRES_AWS_S3_ENDPOINT='' \
           POSTGRES_AWS_S3_S3V4=''

# Operating System
RUN        apk update \
           && apk add --no-cache \
               postgresql \
               python3 \
               curl \
           && pip3 install --no-cache-dir --upgrade pip setuptools wheel \
           && pip3 install --no-cache-dir \
               awscli

# Application
WORKDIR	   /opt/docker

ADD        scripts/backup_postgres_to_s3.sh backup_postgres_to_s3.sh
RUN        chmod +x backup_postgres_to_s3.sh

ADD        scripts/docker-cmd.sh docker-cmd.sh
RUN        chmod +x docker-cmd.sh

CMD        ["./docker-cmd.sh"]