FROM alpine:3.12

# Load ash profile on launch
ENV ENV="/etc/profile"

# Set the timezone and PHP ini settings
ENV TIMEZONE=UTC \
    PHP_MEMORY_LIMIT=256M \
    MAX_UPLOAD=100M \
    PHP_MAX_FILE_UPLOAD=50 \
    PHP_MAX_POST=100M

ENV DD_SERVICE=laquerlabs \
    DD_TRACE_ENABLED=false \
    DD_TRACE_NO_AUTOLOADER=true \
    DD_DISTRIBUTED_TRACING=false \
    DD_TRACE_STARTUP_LOGS=0 \
    DD_VERSION=0.0.0

# install nginx and php7-fpm
# setup and make the working directories
# setup timezone and delete the tzdata package
# add the www-data user
RUN apk --update --no-cache add wget nginx openssl dumb-init tzdata shadow \
    php7-fpm php7-json php7-gd php7-curl php7-dom php7-exif php7-gd \
    php7-iconv php7-imagick php7-json php7-mbstring php7-mysqli \
    php7-opcache php7-ctype php7-simplexml php7-xml php7-xmlreader && \
    mkdir -p /app /run/nginx /run/php7 && \
    cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
    echo "${TIMEZONE}" > /etc/timezone && \
    apk del tzdata

# Manually make some changes for the PHP.INI file
RUN sed -i "s|;*date.timezone =.*|date.timezone = ${TIMEZONE}|i" /etc/php7/php.ini && \
    sed -i "s|;*memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|i" /etc/php7/php.ini && \
    sed -i "s|;*upload_max_filesize =.*|upload_max_filesize = ${MAX_UPLOAD}|i" /etc/php7/php.ini && \
    sed -i "s|;*max_file_uploads =.*|max_file_uploads = ${PHP_MAX_FILE_UPLOAD}|i" /etc/php7/php.ini && \
    sed -i "s|;*post_max_size =.*|post_max_size = ${PHP_MAX_POST}|i" /etc/php7/php.ini && \
    sed -i "s|;*cgi.fix_pathinfo=.*|cgi.fix_pathinfo= 0|i" /etc/php7/php.ini && \
    sed -i "s|;*error_log = .*|error_log = \/proc\/self\/fd\/1|i" /etc/php7/php.ini

# add datadog-php-tracer
RUN wget -O /tmp/datadog-php-tracer_0.47.1_noarch.apk https://github.com/DataDog/dd-trace-php/releases/download/0.47.1/datadog-php-tracer_0.47.1_noarch.apk && \
    apk add /tmp/datadog-php-tracer_0.47.1_noarch.apk --allow-untrusted

# copy our config files over to the container
COPY ./configs /

RUN mv /etc/profile.d/color_prompt /etc/profile.d/color_prompt.sh && \
    chmod a+x /etc/profile.d/aliases.sh /entrypoint.sh && \
    groupmod -g 1001 www-data && \
    usermod -u 1001 -g 1001 -d /run/nginx nginx && \
    chown -R nginx:www-data /run/nginx /run/php7 /app && \
    chmod -R g+srwx /run/nginx /run/php7 /app && \
    apk del shadow

# setup our working directory
# copy over working code
WORKDIR /app
COPY --chown=1001:1001 ./code .

# Setup Volume for persistance
VOLUME /app

# expose our service port
EXPOSE 8080

STOPSIGNAL SIGTERM

USER nginx

# start with our PID 1 controller
ENTRYPOINT [ "/entrypoint.sh" ]

# what we use to start the container
CMD [ "service" ]
