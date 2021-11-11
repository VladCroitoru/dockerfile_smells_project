FROM mwaeckerlin/ubuntu-base

EXPOSE 80
ENV MEMORY_LIMIT "1000M"
ENV UPLOAD_MAX_FILESIZE "8G"
ENV MAX_INPUT_TIME "3600"
ENV WEBROOT ""
ENV ADMIN_USER ""
ENV ADMIN_PWD ""
ENV HOST ""
ENV PROTOCOL "https"
ENV DEBUG "0"

# compile time variables
ENV CONTAINERNAME "nextcloud"
ENV INSTBASE "/var/www"
ENV INSTDIR "${INSTBASE}/nextcloud"
ENV DATADIR "${INSTDIR}/data"
ENV CONFDIR "${INSTDIR}/config"
ENV APPSDIR "${INSTDIR}/apps"
ENV SOURCE_FILE="latest.tar.bz2"
# test if 13.0.0 is fixed: https://github.com/nextcloud/server/issues/8240
#ENV SOURCE_FILE="nextcloud-12.0.5.tar.bz2"
ENV SOURCE="https://download.nextcloud.com/server/releases/${SOURCE_FILE}"
WORKDIR /tmp

ADD health.sh /health.sh
HEALTHCHECK --interval=30s --timeout=10s --start-period=300s --retries=240 CMD /health.sh
ADD nextcloud.asc /nextcloud.asc
ADD start.sh /start.sh
ADD nextcloud.conf /nextcloud.conf

# libmagickcore-extra php-mcrypt
RUN apt-get update \
 && apt-get install --no-install-recommends --no-install-suggests -y \
       gnupg bzip2 pwgen sudo apache2 libapache2-mod-php php-gd \
       php-json php-mysql php-curl php-mbstring php-intl \
       php-imagick php-xml php-zip php-apcu php-ldap \
       rsync php-imagick wget cron mysql-client php-bcmath php-gmp \
 && /cleanup.sh \
 && mkdir -p "${INSTDIR}" \
 && wget -qO${SOURCE_FILE} ${SOURCE} \
 && wget -qO${SOURCE_FILE}.asc ${SOURCE}.asc \
 && gpg --import /nextcloud.asc \
 && gpg --verify ${SOURCE_FILE}.asc ${SOURCE_FILE} \
 && cd "${INSTBASE}" \
 && tar xf /tmp/${SOURCE_FILE} \
 && rm /tmp/${SOURCE_FILE} /tmp/${SOURCE_FILE}.asc /nextcloud.asc \
 && cd "${INSTDIR}" \
 && chmod +x occ \
 && mkdir data \
 && chown -R www-data "${INSTDIR}" config apps data \
 && mv $APPSDIR ${APPSDIR}.original \
 && mkdir $APPSDIR \
 && touch /etc/apache2/conf-available/nextcloud.conf \
 && chown -R www-data.www-data $APPSDIR ${APPSDIR}.original $CONFDIR $DATADIR ${INSTDIR}/.htaccess /etc/apache2/conf-available/nextcloud.conf \
 && ln -sf /proc/1/fd/1 /var/log/apache2/access.log \
 && ln -sf /proc/1/fd/2 /var/log/apache2/error.log \
 && ln -sf /proc/1/fd/1 /var/log/nextcloud.log

VOLUME $DATADIR
VOLUME $CONFDIR
VOLUME $APPSDIR
WORKDIR $INSTDIR
