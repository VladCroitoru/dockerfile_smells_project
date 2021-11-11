FROM xtremxpert/docker-phpapache:latest

MAINTAINER Xtremxpert <xtremxpert@xtremxpert.com>

ENV JOOMLA_VERSION="3.4.5" \
    JOOMLA_SHA1="098ce53f3bc44531be95c20a0faf7f80efe5fc88"

RUN curl -o joomla.zip -SL https://github.com/joomla/joomla-cms/releases/download/${JOOMLA_VERSION}/Joomla_${JOOMLA_VERSION}-Stable-Full_Package.zip \
    && echo "$JOOMLA_SHA1 *joomla.zip" | sha1sum -c - \
    && unzip joomla.zip -d /var/www/htdocs \
    && rm joomla.zip \
    && mv /var/www/htdocs/htaccess.txt /var/www/htdocs/.htaccess \
    && rm /var/www/htdocs/web.config.txt \
    && chown -R apache:apache /var/www/htdocs

EXPOSE 80
EXPOSE 443

VOLUME [/var/www/htdocs]

ENTRYPOINT ["/usr/sbin/httpd"]
CMD ["-DFOREGROUND"]
