FROM debian:8.10
WORKDIR /usr/src

COPY ssh_config /etc/ssh/ssh_config

# Found at: https://www.aptible.com/support/toolbelt/#download-debian
ENV URL "https://omnibus-aptible-toolbelt.s3.amazonaws.com/aptible/omnibus-aptible-toolbelt/master/206/pkg/aptible-toolbelt_0.16.5%2B20200508143650~debian.8.10-1_amd64.deb"
RUN apt-get update \
    && apt-get install -y curl \
    && curl -o aptible-cli.deb "$URL" \
    && dpkg -i aptible-cli.deb \
    && rm -rf /var/lib/apt/lists/* \
    && rm -f aptible-cli.deb

# Used to simplify docker run commands needing the login
COPY run_with_login .

ENTRYPOINT ["aptible"]
CMD ["help"]
