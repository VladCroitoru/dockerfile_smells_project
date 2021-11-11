FROM debian:buster

ARG ODOO_UID=3328
ARG ODOO_GID=3328
ARG ODOO_HOMEDIR=/var/lib/odoo
ENV ODOO_HOMEDIR=${ODOO_HOMEDIR}

ENV ODOO_DB=odoodb
ENV ODOO_CONF_FILE=${ODOO_HOMEDIR}/odoo.conf
ENV ODOO_UPD_FILE=${ODOO_HOMEDIR}/update.txt
ENV ODOO_REQ_FILE=${ODOO_HOMEDIR}/requirements.txt
ENV ODOO_ADMIN_PASSWD=Db4dm1nSup3rS3cr3tP4ssw0rD

ENV POSTGRES_HOST=db
ENV POSTGRES_USER=odoo
ENV POSTGRES_PASSWORD=Us3rP4ssw0rD

ENV LANG=it_IT.UTF-8

RUN apt update && apt -y --no-install-recommends install \
    build-essential \
    bzip2 \
    curl \
    geoip-database \
    git \
    gnupg \
    libgeoip1 \
    libjpeg-dev \
    libmagic-dev \
    libpq-dev \
    libreoffice \
    libxml2-dev \
    libxslt-dev \
    libzip-dev \
    libldap2-dev \
    libsasl2-dev \
    libwebp-dev \
    locales \
    nano \
    procps \
    python3 \
    python3-dev \
    python3-magic \
    python3-pip \
    python3-setuptools \
    rsync \
    tdsodbc \
    telnet \
    unzip \
    vim \
    wget \
    xsltproc \
    zlib1g-dev && \
    curl -L https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.buster_amd64.deb -o /tmp/wkhtmltopdf.deb && \
    apt -y install /tmp/wkhtmltopdf.deb && \
    rm /tmp/wkhtmltopdf.deb && \
    sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" > /etc/apt/sources.list.d/pgdg.list' && \
    curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt update && \
    apt -y install postgresql-client-11 && \
    apt -y dist-upgrade && \
    rm -rf /var/lib/apt/lists/*

RUN echo "it_IT.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

RUN groupadd -g ${ODOO_GID} odoo && \
    useradd -m -d ${ODOO_HOMEDIR} -s /bin/bash -u ${ODOO_UID} -g ${ODOO_GID} odoo && \
    mkdir -p /etc/odoo && \
    chown -R odoo:odoo /etc/odoo /opt

USER odoo
RUN git clone https://github.com/OCA/OCB.git --depth 1 --branch 12.0 --single-branch /opt/odoo

USER root
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r /opt/odoo/requirements.txt && \
    pip3 install --no-cache-dir /opt/odoo && \
    pip3 install --no-cache-dir pdfkit phonenumbers pudb wheel Unidecode && \
    pip3 install --no-cache-dir git+https://github.com/OCA/openupgradelib.git@master

USER odoo
WORKDIR ${ODOO_HOMEDIR}
EXPOSE 8069 8071 8072
VOLUME ${ODOO_HOMEDIR}

COPY run.sh /run.sh
CMD /bin/bash /run.sh
