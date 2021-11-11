FROM alpine:latest
MAINTAINER Emmanuel Frecon <efrecon@gmail.com>

# Install the latest letsencrypt.sh using git, make sure to remove all "traces"
# that we might have left behind to minimise the size of the final image.
RUN apk add --update-cache git bash curl openssl inotify-tools && \
    git clone https://github.com/lukas2511/letsencrypt.sh.git /opt/repos/letsencrypt && \
    ln -s /opt/repos/letsencrypt/letsencrypt.sh /usr/local/bin/ && \
    rm -rf /opt/repos/letsencrypt/.git && \
    apk del git && \
    rm -rf /var/cache/apk/*

COPY bin/* /letsencrypt/bin/
RUN chmod a+x /letsencrypt/bin/*.sh

# Create separate volumes to, respectively: host the domains.txt file specifying
# which domains to control and renew, the generated certificates and finally
# where to place the challenges.
VOLUME /letsencrypt/config
VOLUME /letsencrypt/certs
VOLUME /letsencrypt/wellknown

# Set the following variable to the email address of the contact responsible for
# the domain:
# ENV EMAIL="admin@domain.com"

# Set the following variable to use the staging environment when testing things
# out (and avoid being blocked from Let's Encrypt).
# ENV STAGING=true

# Set the following variable to specify how often to check for certificate
# renewal (defaults to once a day). But the container checks for updates on the
# file containing the domains.
# ENV PERIOD=86400

# Set the following variable to specify another location for the domains.txt
# file. It defaults to the file called domains.txt in /letsencrypt/config, as
# below.
# ENV DOMAINS=/letsencrypt/config/domains.txt

# Set the following variable to request for a single domain cert, this OVERRIDES
# the DOMAINS variable above (which is the default).
# ENV DOMAIN=www.domain.com

# Set the following variable to specify another location for the directory where
# to place the challenges files.
# ENV WELLKNOWN=/letsencrypt/wellknown

# Set the following variable to specify another location for the directory where
# to place account information (defaults to the subdirectory accounts that hosts
# the domains.txt file).
# ENV ACCOUNTS=/letsencrypt/config/accounts

ENTRYPOINT /letsencrypt/bin/run.sh