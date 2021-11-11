FROM ubuntu:18.04
MAINTAINER Pascal GOUHIER <info@copagex.fr>

# generate locales
RUN apt update && apt -yq install locales && locale-gen en_US.UTF-8 && update-locale
RUN echo 'LANG="en_US.UTF-8"' > /etc/default/locale

# Add the PostgreSQL PGP key to verify their Debian packages.
# It should be the same key as https://www.postgresql.org/media/keys/ACCC4CF8.asc
RUN apt -yq install gnupg && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8

# Add PostgreSQL's repository. It contains the most recent stable release
#     of PostgreSQL.
# install dependencies as distrib packages when system bindings are required
# some of them extend the basic odoo requirements for a better "apps" compatibility
# most dependencies are distributed as wheel packages at the next step
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
  apt update && \
  apt -yq install \
    adduser \
    ghostscript \
    postgresql-client-10 \
    python \
    python-pip \
    python-pil \
    python-pychart python-libxslt1 xfonts-base xfonts-75dpi \
    libxrender1 libxext6 fontconfig \
    python-zsi \
    python-lasso \
    libzmq5 \
    # libpq-dev is needed to install pg_config which is required by psycopg2
    libpq-dev \
    # These libraries are needed to install the pip modules
    python-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    libldap2-dev \
    libsasl2-dev \
    libssl-dev \
    # Librairies required for LESS
    node-less \
    nodejs \
    node-gyp \
    npm \
    # This library is necessary to upgrade PIL/pillow module
    libjpeg8-dev \
    # Git is required to clone Odoo OCB project
    git \
    # Utilities
    wget \
    nano

RUN pip install --upgrade pip

# create the odoo user
RUN adduser --home=/opt/odoo --disabled-password --gecos "" --shell=/bin/bash odoo

# changing user is required by openerp which won't start with root
# makes the container more unlikely to be unwillingly changed in interactive mode
USER odoo

RUN /bin/bash -c "mkdir -p /opt/odoo/{bin,etc,sources/odoo,addons/CE_inherited,addons/external,addons/nonfree,addons/private,data}"
RUN /bin/bash -c "mkdir -p /opt/odoo/var/{run,log,egg-cache}"

# Add Odoo OCB sources and remove .git folder in order to reduce image size
WORKDIR /opt/odoo/sources
RUN git clone https://github.com/OCA/OCB.git -b 12.0 odoo && \
  rm -rf odoo/.git

USER root
# Install Odoo python dependencies
RUN pip install -r /opt/odoo/sources/odoo/requirements.txt

# SM: Install LESS
RUN npm install -g less less-plugin-clean-css && \
  ln -s /usr/bin/nodejs /usr/bin/node

# must unzip this package to make it visible as an odoo external dependency
RUN easy_install -UZ py3o.template

# install wkhtmltopdf based on QT5
# Warning: do not use latest version (0.12.2.1) because it causes the footer issue (see https://github.com/odoo/odoo/issues/4806)
ADD https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb /opt/sources/wkhtmltox.deb
RUN dpkg -i /opt/sources/wkhtmltox.deb && apt install -f

# Execution environment
USER 0
ADD sources/odoo.conf /opt/sources/odoo.conf
WORKDIR /app

# Add volumes. For addons :
# "/opt/odoo/addons/CE_inherited" : adapted modules from Odoo official Community version,
# "/opt/odoo/addons/external" : Community modules (OCA or others),
# "/opt/odoo/addons/nonfree" : non free modules (paid themes for example), and your own modules wich depend from nonfree module(s)
# "/opt/odoo/addons/private" : your own modules from scratch, even if they depend from other (community) modules
VOLUME ["/opt/odoo/var", "/opt/odoo/etc", "/opt/odoo/addons/CE_inherited","/opt/odoo/addons/external","/opt/odoo/addons/nonfree","/opt/odoo/addons/private", "/opt/odoo/data"]

# Set the default entrypoint (non overridable) to run when starting the container
ADD bin/boot /app/bin/boot
ENTRYPOINT ["/app/bin/boot"]
CMD ["help"]
# Expose the odoo ports (for linked containers)
EXPOSE 8069 8072

