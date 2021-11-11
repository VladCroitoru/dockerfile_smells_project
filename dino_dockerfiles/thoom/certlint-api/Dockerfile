#
# CertLint web-service docker image
#
FROM ruby:alpine
MAINTAINER Z.d.Peacock <zdp@thoomtech.com>

#
# Install certlint and asn1c
#
COPY certlint /usr/local/certlint
COPY asn1c    /usr/local/certlint/ext/asn1c

COPY asn1c-installer.sh /tmp

#
# Install pre-requisite packages for building asn1c
# Store the build dependencies so that they can be removed later
#
RUN apk add --no-cache --update --virtual .build-deps \
    build-base automake git patch libtool  autoconf curl \
    && apk add --no-cache --update libstdc++ \
    # Once these files are in place, run the shell script to build asn1c
    && sh /tmp/asn1c-installer.sh \
    && rm /tmp/asn1c-installer.sh \
    #
    # Required ruby gems (-N doesn't install ruby documentation)
    #  - certlint:  public_suffix simpleidn
    #  - web-service: sinatra thin
    #
    && gem install -N public_suffix simpleidn sinatra thin \
    # Remove leftover build dependencies
    && apk del .build-deps

# Save the API to the correct location
WORKDIR /server
COPY api .

EXPOSE 9000

CMD ["thin", "-R", "config.ru", "-p", "9000", "start"]
