# Default ARG values which may be overriden in build command with
# docker-compose build --build-arg KEY=VAL
#  as in 
# make init && make build ARGS="--build-arg MIG_SVN_REV=HEAD"
#  or using
# docker-compose build
# with .env file in place
#
# IMPORTANT: all ARGS here that should allow being overriden from .env MUST be
#            explicitly listed in docker-compose.yml *args* list, too.
#            Furthermore they must be declared after FROM in each stage used.

ARG BUILD_TYPE=basic
ARG BUILD_TARGET=development
ARG DOMAIN=migrid.test
ARG MIG_SVN_REPO=https://svn.code.sf.net/p/migrid/code/trunk
ARG MIG_SVN_REV=5250
ARG MIG_GIT_REPO=https://github.com/ucphhpc/migrid-sync.git
ARG MIG_GIT_BRANCH=master
ARG MIG_GIT_REV=047a4002d11b5743141b6cef3ec93672f9f30098
ARG EMULATE_FLAVOR=migrid
ARG EMULATE_FQDN=migrid.org
ARG WITH_PY3=no
ARG WITH_GIT=no

# Jupyter Arguments
ARG JUPYTER_SERVICES=""
ARG JUPYTER_SERVICES_DESC="{}"

FROM centos:7 as init
ARG BUILD_TYPE
#ARG BUILD_TARGET
ARG DOMAIN
#ARG MIG_SVN_REPO
#ARG MIG_SVN_REV
#ARG MIG_GIT_REPO
#ARG MIG_GIT_BRANCH
#ARG MIG_GIT_REV
#ARG EMULATE_FLAVOR
#ARG EMULATE_FQDN
ARG WITH_PY3
ARG JUPYTER_SERVICES
#ARG WITH_GIT

RUN echo "Build type: $BUILD_TYPE"
#RUN echo "Build target: $BUILD_TARGET"
RUN echo "Domain: $DOMAIN"
#RUN echo "MiG svn repo and revision: $MIG_SVN_REPO $MIG_SVN_REV"
#RUN echo "MiG git repo , branch and revision: $MIG_GIT_REPO $MIG_GIT_BRANCH $MIG_GIT_REV"
#RUN echo "Emulate flavor: $EMULATE_FLAVOR"
#RUN echo "Emulate FQDN: $EMULATE_FQDN"
RUN echo "Enable python3 support: $WITH_PY3"
#RUN echo "Designated jupyter services: $JUPYTER_SERVICES"
#RUN echo "Enable git checkout: $WITH_GIT"

FROM init as base
ARG DOMAIN
ARG WITH_PY3

WORKDIR /tmp

# Centos image default yum configs prevent docs installation
# https://superuser.com/questions/784451/centos-on-docker-how-to-install-doc-files
RUN sed -i '/nodocs/d' /etc/yum.conf

RUN yum update -y \
    && yum install -y epel-release \
    && yum clean all \
    && rm -fr /var/cache/yum

RUN yum update -y \
    && yum install -y \
    gcc \
    pam-devel \
    httpd \
    htop \
    openssh \
    crontabs \
    nano \
    mod_ssl \
    mod_wsgi \
    mod_proxy \
    mod_auth_openid \
    tzdata \
    initscripts \
    svn \
    git \
    vim \
    net-tools \
    telnet \
    ca-certificates \
    mercurial \
    openssh-server \
    openssh-clients \
    rsyslog \
    lsof \
    python-pip \
    python-devel \
    python-paramiko \
    python-enchant \
    python-jsonrpclib \
    python-requests \
    python2-psutil \
    python-future \
    python2-cffi \
    pysendfile \
    PyYAML \
    pyOpenSSL \
    # NOTE: generally install cracklib from pip as yum only has py2 version
    #cracklib-python \
    cracklib-devel \
    lftp \
    rsync \
    fail2ban \
    ipset \
    wget

RUN if [ "${WITH_PY3}" = "yes" ]; then \
      echo "install py3 deps" \
      && yum update -y \
      && yum install -y \
      python3-pip \
      python3-devel \
      python3-mod_wsgi \
      #python3-paramiko \
      python36-paramiko \
      #python3-enchant \
      #python3-jsonrpclib \
      #python3-requests \
      python36-requests \
      #python3-psutil \
      python36-psutil \
      python3-future \
      #python3-cffi \
      python36-cffi \
      python36-pyOpenSSL \
      python36-PyYAML; \
    else \
      echo "no py3 deps"; \
    fi;

# Apache OpenID (provided by epel)
RUN yum install -y mod_auth_openid

# Setup container default language to make sure UTF8 is available in wsgi app.
# Otherwise sys.getfilesystemencoding will return ascii despite utf8 FS, and
# thus result e.g. in broken user path and client_id for users with accented
# chars e.g. in their name.
# https://stackoverflow.com/a/28212946
# TODO: do we need to generate this rather common locale? (looks like no)
#RUN localedef -c -i en_US -f UTF-8 en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

# Setup user
ENV USER=mig
ENV UID=1000
ENV GID=1000

RUN groupadd -g $GID $USER
RUN useradd -u $UID -g $GID -ms /bin/bash $USER

# MiG environment
ENV MIG_ROOT=/home/$USER
ENV WEB_DIR=/etc/httpd
ENV CERT_DIR=$WEB_DIR/MiG-certificates

USER root

RUN mkdir -p $CERT_DIR/MiG/*.$DOMAIN \
    && chown $USER:$USER $CERT_DIR \
    && chmod 775 $CERT_DIR

# Certs and keys
FROM base as setup_security
ARG DOMAIN

# Dhparam - https://wiki.mozilla.org/Security/Archive/Server_Side_TLS_4.0
RUN curl https://ssl-config.mozilla.org/ffdhe4096.txt -o $CERT_DIR/dhparams.pem

# CA
# https://gist.github.com/Soarez/9688998
RUN openssl genrsa -des3 -passout pass:qwerty -out ca.key 2048 \
    && openssl rsa -passin pass:qwerty -in ca.key -out ca.key \
    && openssl req -x509 -new -key ca.key \
    -subj "/C=DK/ST=NA/L=NA/O=MiGrid-Test/OU=NA/CN=*.${DOMAIN}" -out ca.crt \
    && openssl req -x509 -new -nodes -key ca.key -sha256 -days 1024 \
    -subj "/C=DK/ST=NA/L=NA/O=MiGrid-Test/OU=NA/CN=*.${DOMAIN}" -out ca.pem

# Server key/ca
# https://gist.github.com/Soarez/9688998
RUN openssl genrsa -out server.key 2048 \
    && openssl req -new -key server.key -out server.csr \
    -subj "/C=DK/ST=NA/L=NA/O=MiGrid-Test/OU=NA/CN=*.${DOMAIN}" \
    && openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

# CRL
RUN touch /etc/pki/CA/index.txt \
    && echo '00' > /etc/pki/CA/crlnumber \
    && openssl ca -gencrl -keyfile ca.key -cert ca.pem -out crl.pem

# Daemon keys
RUN cat server.{key,crt} > combined.pem \
    && cat server.crt > server.ca.pem \
    && cat ca.pem >> server.ca.pem \
    && chown $USER:$USER combined.pem \
    && chown $USER:$USER server.ca.pem \
    && ssh-keygen -y -f combined.pem > combined.pub \
    && chown 0:0 *.key server.crt ca.pem \
    && chmod 400 *.key server.crt ca.pem combined.pem server.ca.pem

# Prepare keys for mig
RUN mv server.crt $CERT_DIR/MiG/*.$DOMAIN/ \
    && mv server.key $CERT_DIR/MiG/*.$DOMAIN/ \
    && mv crl.pem $CERT_DIR/MiG/*.$DOMAIN/ \
    && mv ca.pem $CERT_DIR/MiG/*.$DOMAIN/cacert.pem \
    && mv combined.pem $CERT_DIR/MiG/*.$DOMAIN/ \
    && mv combined.pub $CERT_DIR/MiG/*.$DOMAIN/ \
    && mv server.ca.pem $CERT_DIR/MiG/*.$DOMAIN/

WORKDIR $CERT_DIR

RUN ln -s MiG/*.$DOMAIN/server.crt server.crt \
    && ln -s MiG/*.$DOMAIN/server.key server.key \
    && ln -s MiG/*.$DOMAIN/crl.pem crl.pem \
    && ln -s MiG/*.$DOMAIN/cacert.pem cacert.pem \
    && ln -s MiG/*.$DOMAIN/combined.pem combined.pem \
    && ln -s MiG/*.$DOMAIN/server.ca.pem server.ca.pem \
    && ln -s MiG/*.$DOMAIN/combined.pub combined.pub \
    && ln -s MiG/*.$DOMAIN www.$DOMAIN \
    && ln -s MiG/*.$DOMAIN cert.$DOMAIN \
    && ln -s MiG/*.$DOMAIN ext.$DOMAIN \
    && ln -s MiG/*.$DOMAIN oid.$DOMAIN \
    && ln -s MiG/*.$DOMAIN sid.$DOMAIN \
    && ln -s MiG/*.$DOMAIN io.$DOMAIN \
    && ln -s MiG/*.$DOMAIN openid.$DOMAIN \
    && ln -s MiG/*.$DOMAIN sftp.$DOMAIN \
    && ln -s MiG/*.$DOMAIN ftps.$DOMAIN \
    && ln -s MiG/*.$DOMAIN webdavs.$DOMAIN

# Upgrade pip, required by cryptography
RUN python -m pip install -U pip==20.3.4

WORKDIR $MIG_ROOT
USER $USER

RUN mkdir -p MiG-certificates \
    && cd MiG-certificates \
    && ln -s $CERT_DIR/MiG/*.$DOMAIN/cacert.pem cacert.pem \
    && ln -s $CERT_DIR/MiG MiG \
    && ln -s $CERT_DIR/combined.pem combined.pem \
    && ln -s $CERT_DIR/combined.pub combined.pub \
    && ln -s $CERT_DIR/dhparams.pem dhparams.pem


FROM setup_security as mig_dependencies
ARG DOMAIN
ARG ENABLE_DEFAULT_PY
ARG WITH_PY3

# Prepare OpenID (python-openid for py2 and python-openid2 for py3)
ENV PATH=$PATH:/home/$USER/.local/bin
RUN pip install --user python-openid
RUN if [ "$WITH_PY3" = "yes" ]; then \
      echo "install py3 openid" \
      pip3 install --user python-openid2; \
    fi;

# Modules required by grid_events.py
RUN pip install --user \
    watchdog \
    scandir
RUN if [ "$WITH_PY3" = "yes" ]; then \
      pip3 install --user \
      watchdog; \
    fi;

# Modules required by grid_webdavs
# NOTE: we require <=1.3.0 for python2. CherryPy is no longer bundled lately.
RUN pip install --user \
    wsgidav==1.3.0
RUN if [ "$WITH_PY3" = "yes" ]; then \
      pip3 install --user \
      wsgidav cherrypy; \
    fi;

# Modules required by grid_ftps
# NOTE: relies on pyOpenSSL and Cryptography from yum for now
RUN pip install --user \
    pyftpdlib
RUN if [ "$WITH_PY3" = "yes" ]; then \
      pip3 install --user \
      pyftpdlib; \
    fi;

# Modules required by grid_X IO daemons (not availalble in yum for py 3)
RUN pip install --user \
    cracklib
RUN if [ "$WITH_PY3" = "yes" ]; then \
      pip3 install --user \
      cracklib; \
    fi;

# Modules required by jupyter
#RUN pip install --user \
#    requests

# Module required to run pytests
# 4.6 is the latest with python2 support
RUN pip install --user \
    pytest
RUN if [ "$WITH_PY3" = "yes" ]; then \
      pip3 install --user \
      pytest; \
    fi;

# Modules required by 2FA
# NOTE: we require <=2.3.0 for python2.
RUN pip install --user \
    pyotp==2.3.0
RUN if [ "$WITH_PY3" = "yes" ]; then \
      pip3 install --user \
      pyotp; \
    fi;

# Modules required for smart country selection
RUN pip install --user \
    iso3166
RUN if [ "$WITH_PY3" = "yes" ]; then \
      pip3 install --user \
      iso3166; \
    fi;

FROM mig_dependencies as download_mig
ARG DOMAIN
ARG MIG_SVN_REPO
ARG MIG_SVN_REV
ARG WITH_GIT
ARG MIG_GIT_REPO
ARG MIG_GIT_BRANCH
ARG MIG_GIT_REV

# Install and configure MiG
# NOTE: git refuses to clone into non-empty dir - use tmp
#     cd migrid.git && git checkout --track origin/${MIG_GIT_BRANCH} ${MIG_GIT_REV} && cd .. ; \

RUN if [ "$WITH_GIT" = "yes" ]; then \
      git clone ${MIG_GIT_REPO} migrid.git && \
        cd migrid.git && \
        git checkout -B ${MIG_GIT_BRANCH} --track origin/${MIG_GIT_BRANCH} && \
        git checkout ${MIG_GIT_REV} && cd .. && \
        rsync -a migrid.git/ ./ && \
        rm -rf migrid.git/ ; \
    else \
      svn checkout -r ${MIG_SVN_REV} ${MIG_SVN_REPO} . ; \
    fi;

ADD --chown=$USER:$USER mig $MIG_ROOT/

FROM download_mig as install_mig
ARG DOMAIN
ARG EMULATE_FLAVOR
ARG EMULATE_FQDN
ARG JUPYTER_SERVICES
ARG JUPYTER_SERVICES_DESC

ENV PYTHONPATH=${MIG_ROOT}
# Ensure that the $USER sets it during session start
RUN echo "PYTHONPATH=${MIG_ROOT}" >> ~/.bash_profile \
    && echo "export PYTHONPATH" >> ~/.bash_profile

WORKDIR $MIG_ROOT/mig/install

RUN echo "Designated jupyter services: $JUPYTER_SERVICES"
RUN echo "Designated jupyter services descriptions: $JUPYTER_SERVICES_DESC"

RUN ./generateconfs.py --source=. \
    --destination=generated-confs \
#    --destination_suffix="_svn$(svnversion -n ~/)" \
    --base_fqdn=$DOMAIN \
    --public_fqdn=www.$DOMAIN \
    --mig_cert_fqdn=cert.$DOMAIN \
    --ext_cert_fqdn= \
    --mig_oid_fqdn=ext.$DOMAIN \
    --ext_oid_fqdn= \
    --sid_fqdn=sid.$DOMAIN \
    --io_fqdn=io.$DOMAIN \
    --user=mig --group=mig \
    --apache_version=2.4 \
    --apache_etc=/etc/httpd \
    --apache_run=/var/run/httpd \
    --apache_lock=/var/lock/subsys/httpd \
    --apache_log=/var/log/httpd \
    --openssh_version=7.4 \
    --mig_code=/home/mig/mig \
    --mig_state=/home/mig/state \
    --mig_certs=/etc/httpd/MiG-certificates \
    --hg_path=/usr/bin/hg \
    --hgweb_scripts=/usr/share/doc/mercurial-2.6.2 \
    --trac_admin_path= \
    --trac_ini_path= \
    --openid_address=openid.$DOMAIN \
    --sftp_address=sftp.$DOMAIN \
    --sftp_subsys_address=sftp.$DOMAIN \
    --ftps_address=ftps.$DOMAIN \
    --davs_address=webdavs.$DOMAIN \
    --public_http_port=80 --public_https_port=444 \
    --mig_oid_port=443 --ext_oid_port=445 \
    --mig_cert_port=446 --ext_cert_port=447 \
    --sid_port=448 \
    --sftp_port=2222 --sftp_subsys_port=22222 \
    --mig_oid_provider=https://ext.$DOMAIN/openid/ \
    --ext_oid_provider= \
    --enable_openid=True --enable_wsgi=True \
    --enable_sftp=True --enable_sftp_subsys=True \
    --enable_davs=True --enable_ftps=True \
    --enable_sharelinks=True --enable_transfers=True \
    --enable_duplicati=True --enable_seafile=False \
    --enable_sandboxes=False --enable_vmachines=False \
    --enable_crontab=True --enable_jobs=True \
    --enable_resources=True --enable_events=True \
    --enable_freeze=False --enable_imnotify=False \
    --enable_twofactor=True --enable_cracklib=True \
    --enable_notify=True --enable_preview=False \
    --enable_workflows=False --enable_hsts=True \
    --enable_vhost_certs=True --enable_verify_certs=True \
    --enable_jupyter=True \
    --jupyter_services=${JUPYTER_SERVICES} \
    "--jupyter_services_desc=${JUPYTER_SERVICES_DESC}" \
    --user_clause=User --group_clause=Group \
    --listen_clause='#Listen' \
    --serveralias_clause='ServerAlias' --alias_field=email \
    --dhparams_path=~/certs/dhparams.pem \
    --daemon_keycert=~/certs/combined.pem \
    --daemon_pubkey=~/certs/combined.pub \
    --daemon_pubkey_from_dns=False \
    --daemon_show_address=io.$DOMAIN \
    --signup_methods="migoid migcert" \
    --login_methods="migoid migcert" \
    --distro=centos --user_interface="V3 V2" \
    --skin=${EMULATE_FLAVOR}-basic --short_title="MiGrid-Test" \
    --vgrid_label=Workgroup \
    --apache_worker_procs=256 --wsgi_procs=25

RUN cp generated-confs/MiGserver.conf $MIG_ROOT/mig/server/ \
    && cp generated-confs/static-skin.css $MIG_ROOT/mig/images/ \
    && cp generated-confs/index.html $MIG_ROOT/state/user_home/ \
    && cp $MIG_ROOT/mig/images/site-conf-${EMULATE_FQDN}.js $MIG_ROOT/mig/images/site-conf.js


FROM install_mig as setup_mig_configs
ARG DOMAIN
ARG EMULATE_FLAVOR
ARG EMULATE_FQDN

# Enable jupyter menu
RUN sed -i -e 's/#user_menu =/user_menu = jupyter/g' $MIG_ROOT/mig/server/MiGserver.conf \
    && sed -i -e 's/loglevel = info/loglevel = debug/g' $MIG_ROOT/mig/server/MiGserver.conf

# Prepare oiddiscover for httpd
RUN cd $MIG_ROOT/mig \
    && python shared/httpsclient.py | grep -A 80 "xml version" \
    > $MIG_ROOT/state/wwwpublic/oiddiscover.xml

USER root

# Sftp subsys config
RUN cp generated-confs/sshd_config-MiG-sftp-subsys /etc/ssh/ \
    && chown 0:0 /etc/ssh/sshd_config-MiG-sftp-subsys

# PAM and NSS setup for sftpsubsys login to work
RUN cd $MIG_ROOT/mig/src/libpam-mig \
    && make && make install
RUN cd $MIG_ROOT/mig/src/libnss-mig \
    && make && make install

RUN cp generated-confs/libnss_mig.conf /etc/ \
    #&& cp /etc/pam.d/sshd /etc/pam.d/sshd.backup \
    && cp generated-confs/pam-sshd /etc/pam.d/sshd \
    #&& cp /etc/nsswitch.conf /etc/nsswitch.conf.backup
    && cp generated-confs/nsswitch.conf /etc/

RUN chmod 755 generated-confs/envvars \
    && chmod 755 generated-confs/httpd.conf

# Automatic inclusion confs
RUN cp generated-confs/MiG.conf $WEB_DIR/conf.d/ \
    && cp generated-confs/httpd.conf $WEB_DIR/ \
    && cp generated-confs/mimic-deb.conf $WEB_DIR/conf/httpd.conf \
    && cp generated-confs/envvars /etc/sysconfig/httpd \
    && cp generated-confs/apache2.service /lib/systemd/system/httpd.service

# Automatic Jupyter inclusion confs
RUN mkdir -p $WEB_DIR/conf.extras.d/ \
    && cp generated-confs/MiG-jupyter-def.conf /etc/httpd/conf.extras.d \
    && cp generated-confs/MiG-jupyter-openid.conf /etc/httpd/conf.extras.d \
    && cp generated-confs/MiG-jupyter-proxy.conf /etc/httpd/conf.extras.d \
    && cp generated-confs/MiG-jupyter-rewrite.conf /etc/httpd/conf.extras.d

# Root confs
RUN cp generated-confs/apache2.conf $WEB_DIR/ \
    && cp generated-confs/ports.conf $WEB_DIR/ \
    && cp generated-confs/envvars $WEB_DIR/

# Disable certificate check for OID
RUN sed -i '/\/server.ca.pem/ a SSLProxyCheckPeerName off' $WEB_DIR/conf.d/MiG.conf \
    && sed -i '/SSLProxyCheckPeerName off/ a SSLProxyCheckPeerCN off' \
    $WEB_DIR/conf.d/MiG.conf

# Front page
RUN ln -s index-${EMULATE_FQDN}.html $MIG_ROOT/state/wwwpublic/index.html && \
    ln -s about-${EMULATE_FQDN}.html $MIG_ROOT/state/wwwpublic/about-snippet.html && \
    ln -s support-${EMULATE_FQDN}.html $MIG_ROOT/state/wwwpublic/support-snippet.html && \
    ln -s tips-${EMULATE_FQDN}.html $MIG_ROOT/state/wwwpublic/tips-snippet.html && \
    ln -s terms-${EMULATE_FQDN}.html $MIG_ROOT/state/wwwpublic/terms-snippet.html && \
    chown -R $USER:$USER $MIG_ROOT/state/wwwpublic/*.html

# Replace index.html redirects to development domain RUN
RUN sed -i -e "s/${EMULATE_FQDN}/$DOMAIN/g" $MIG_ROOT/state/wwwpublic/index.html

# State clean services
RUN chmod 755 generated-confs/{migstateclean,migerrors} \
    && cp generated-confs/{migstateclean,migerrors} /etc/cron.daily/

# Logrotate config
RUN cp generated-confs/logrotate-migrid /etc/logrotate.d/migrid

# Init scripts
RUN cp generated-confs/migrid-init.d-rh /etc/init.d/migrid

WORKDIR $MIG_ROOT

# Prepare default conf.d
RUN mv $WEB_DIR/conf.d/autoindex.conf $WEB_DIR/conf.d/autoindex.conf.centos \
    && mv $WEB_DIR/conf.d/ssl.conf $WEB_DIR/conf.d/ssl.conf.centos \
    && mv $WEB_DIR/conf.d/userdir.conf $WEB_DIR/conf.d/userdir.conf.centos \
    && mv $WEB_DIR/conf.d/welcome.conf $WEB_DIR/conf.d/welcome.conf.centos

# Add generated certificate to trust store
RUN update-ca-trust force-enable \
    && cp $CERT_DIR/combined.pem /etc/pki/ca-trust/source/anchors/ \
    && update-ca-trust extract

FROM setup_mig_configs as start_mig
ARG DOMAIN

# Reap defuncted/orphaned processes
ARG TINI_VERSION=v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

ADD docker-entry.sh /app/docker-entry.sh
ADD migrid-httpd.env /app/migrid-httpd.env
RUN chown $USER:$USER /app/docker-entry.sh \
    && chmod +x /app/docker-entry.sh

USER root
WORKDIR /app

# EXPOSE is not important but keep in sync with active ports for the record
EXPOSE 80 443 444 445 446 447 448 2222 4443 8021 22222

CMD ["bash", "/app/docker-entry.sh"]
