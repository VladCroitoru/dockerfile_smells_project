FROM alpine:latest
Label maintainer="Wolfereign"

# Update Packages and Install Needed Packages
RUN apk add --update --no-cache \ 
    dcron \
    wget \
    git \
    rsync \
    curl \
    ca-certificates

# Create extra directories for crontabs
RUN mkdir -p /var/log/cron && \ 
    touch /var/log/cron/cron.log && \
    mkdir -m 0644 -p /etc/cron.d

# Copy entry script and make executable
COPY ./entrypoint.sh /usr/local/bin/
RUN chmod a+x /usr/local/bin/entrypoint.sh

# Set entry script and its arguments
ENTRYPOINT ["entrypoint.sh"]
CMD ["su", "-c", "/usr/sbin/crond -f -d 8"]
