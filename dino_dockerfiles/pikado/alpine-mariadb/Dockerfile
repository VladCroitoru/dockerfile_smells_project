FROM alpine
LABEL maintener="pokido99@gmail.com"

# Proxy settings
# ENV http_proxy http://proxy.domain.com:8080
# ENV https_proxy http://proxy.domain.com:8080
# ENV no_proxy "127.0.0.1,localhost,.domain.com"

# Install MariaDB
RUN apk --no-cache --update add mariadb mariadb-client && \
    rm -f /var/cache/apk/*

ADD run.sh /
RUN chmod +x /run.sh

EXPOSE 3306 

# Define default command
CMD ["/run.sh"]
