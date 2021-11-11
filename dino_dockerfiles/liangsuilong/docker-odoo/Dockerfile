FROM ubuntu:16.04
MAINTAINER Suilong Liang <suilong.liang@worktogether.io>

ENV ODOO_VERSION 10.0
ENV ODOO_RELEASE 20180122
ENV GOSU_VERSION 1.10

RUN groupadd -r odoo  && useradd -r -g odoo odoo

# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf
RUN set -ex; \
	\
	fetchDeps=' \
		ca-certificates \
		wget \
                node-less \
                python-gevent \
                python-pip \
                python-setuptools \
                python-renderpm \
                python-watchdog \
                xz-utils \
	'; \
	apt-get update; \
	apt-get install -y --no-install-recommends $fetchDeps; \
	rm -rf /var/lib/apt/lists/*; \
        wget -O wkhtmltox.tar.xz "https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz"; \
        tar xvf wkhtmltox.tar.xz; \
        cp wkhtmltox/lib/* /usr/local/lib/; \
        cp wkhtmltox/bin/* /usr/local/bin/; \
        cp -r wkhtmltox/share/man/man1 /usr/local/share/man/; \
	rm -f wkhtmltox.tar.xz; \
	rm -rf wkhtmltox/; \
	pip install --upgrade pip; \
	pip install --upgrade setuptools; \
        pip install psycogreen==1.0; \
	dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \
	wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"; \
	\
	chmod +x /usr/local/bin/gosu; \
# verify that the binary works
	gosu nobody true; \
	\
	apt-get purge -y --auto-remove $fetchDeps


# Install Odoo
ENV ODOO_VERSION 10.0
ENV ODOO_RELEASE 20180122
RUN set -x; \
        apt-get update; \
	apt-get  install -y --no-install-recommends wget; \
	wget -O odoo.deb "http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}.${ODOO_RELEASE}_all.deb"; \
	dpkg --force-depends -i odoo.deb; \
	apt-get -y install -f --no-install-recommends; \
	apt-get purge -y --auto-remove wget; \
	rm -rf /var/lib/apt/lists/* odoo.deb

# Copy entrypoint script and Odoo configuration file
ADD entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
COPY ./odoo.conf /etc/odoo/
RUN chown odoo /etc/odoo/odoo.conf

# Mount /var/lib/odoo to allow restoring filestore and /mnt/extra-addons for users addons
RUN mkdir -p /mnt/extra-addons \
        && chown -R odoo /mnt/extra-addons
VOLUME ["/var/lib/odoo", "/mnt/extra-addons", "/opt/odoo"]

# Expose Odoo services
EXPOSE 8069 8072

# Set the default config file
ENV ODOO_RC /etc/odoo/odoo.conf

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["odoo"]
