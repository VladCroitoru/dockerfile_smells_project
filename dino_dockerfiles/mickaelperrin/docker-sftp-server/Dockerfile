FROM alpine
MAINTAINER Mickaël PERRIN <dev@mickaelperrin.fr>

# shadow is required for usermod
# tzdata for time syncing
# bash for entrypoint script
RUN apk add --no-cache openssh bash shadow tzdata

# Ensure key creation
RUN rm -rf /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_dsa_key /etc/ssh/ssh_host_ecdsa_key

# Create entrypoint script
ADD docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
RUN mkdir -p /docker-entrypoint.d

# SSH Server configuration file
ADD sshd_config /etc/ssh/sshd_config
RUN addgroup sftp

# Default environment variables
ENV TZ="Europe/Paris" \
    LANG="C.UTF-8"

EXPOSE 22
ENTRYPOINT [ "/docker-entrypoint.sh" ]

# RUN SSH in no daemon and expose errors to stdout
CMD [ "/usr/sbin/sshd", "-D", "-e" ]
