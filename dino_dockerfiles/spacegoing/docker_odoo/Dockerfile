FROM debian:jessie
ENV REFRESHED_AT 2017-06-15
MAINTAINER spacegoing <spacegoing@github>

# This Dockerfile mainly copy from odoo's official docker file
# but with ipdb ipython and pip>9.0+ installed

# Install some deps, lessc and less-plugin-clean-css, and
# wkhtmltopdf apt-get install python-pip \ this install pip 1.5
# far outdated instead we installed pip 9.0+ directly from source.
# As for ipython, we first install python-dev related packages
# then build ipython.
RUN set -ex && buildDeps='build-essential libssl-dev libffi-dev python-dev' \
        && apt-get update \
        && apt-get install -y --no-install-recommends \
            $buildDeps \
            ca-certificates \
            curl \
            node-less \
            python-gevent \
            python-ipdb \
            python-renderpm \
            python-support \
            python-watchdog \
        && curl -o wkhtmltox.deb -SL http://nightly.odoo.com/extra/wkhtmltox-0.12.1.2_linux-jessie-amd64.deb \
        && echo '40e8b906de658a2221b15e4e8cd82565a47d7ee8 wkhtmltox.deb' | sha1sum -c - \
        && curl https://bootstrap.pypa.io/get-pip.py | python \
        && /usr/local/bin/pip2.7 install 'ipython>=5' \
        && dpkg --force-depends -i wkhtmltox.deb \
        && apt-get -y install -f --no-install-recommends \
        && apt-get purge -y --auto-remove $buildDeps -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false npm \
        && rm -rf /var/lib/apt/lists/* wkhtmltox.deb \
        && pip install psycogreen==1.0

# Install Odoo
# No sha1sum check && echo '5d2fb0cc03fa0795a7b2186bb341caa74d372e82 odoo.deb' | sha1sum -c - \
ENV ODOO_VERSION 10.0
ENV ODOO_RELEASE 20170615
RUN set -ex; \
        curl -o odoo.deb -SL http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}.${ODOO_RELEASE}_all.deb \
        && dpkg --force-depends -i odoo.deb \
        && apt-get update \
        && apt-get -y install -f --no-install-recommends \
        && rm -rf /var/lib/apt/lists/* odoo.deb

# Copy entrypoint script
COPY ./entrypoint.sh /
# My Odoo configuration file
COPY ./config/odoo.conf /etc/odoo/
# My Odoo Helper bash commands
RUN mkdir /my_bin
COPY ./.bin/ /my_bin/
# chown chmod of above files
RUN chown odoo /entrypoint.sh && chmod +x /entrypoint.sh \
    && chown odoo /etc/odoo/odoo.conf \
    && chown -R odoo /my_bin && chmod -R 0777 /my_bin

# Mount /var/lib/odoo to allow restoring filestore and /mnt/extra-addons for users addons
RUN mkdir -p /mnt/extra-addons \
        && chown -R odoo /mnt/extra-addons
VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]

# Expose Odoo services
EXPOSE 8069 8071

# Set the default config file
ENV ODOO_RC /etc/odoo/odoo.conf

# Set default user when running the container
USER odoo

# Can't directly `export PATH=$PATH:/my_bin/`
ENV PATH "$PATH:/my_bin"

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]
