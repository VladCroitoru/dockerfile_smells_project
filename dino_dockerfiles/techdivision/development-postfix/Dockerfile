# TechDivision Development Postfix Image
#
# NOTICE OF LICENSE
#
# This source file is subject to the Open Software License (OSL 3.0)
# that is available through the world-wide-web at this URL:
# http://opensource.org/licenses/osl-3.0.php
#
# @author    Vadim Justus <v.justus@techdivision.com>
# @copyright 2016 TechDivision GmbH <info@techdivision.com>
# @license   http://opensource.org/licenses/osl-3.0.php Open Software License (OSL 3.0)
# @link      https://github.com:techdivision/development-postfix.git
# @link      http://www.techdivision.com

FROM alpine:edge

MAINTAINER Vadim Justus <v.justus@techdivision.com>

RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    apk add --no-cache --update \
        postfix \
        postfix-pcre \
        ca-certificates \
        supervisor \
        rsyslog \
        bash && \
    (rm "/tmp/"* 2>/dev/null || true) && (rm -rf /var/cache/apk/* 2>/dev/null || true)

COPY usr/bin/mailhog /usr/bin/mailhog
COPY etc /etc

RUN chmod +x /etc/postfix/start.sh && \
    chmod +x /usr/bin/mailhog

EXPOSE 587 8025

VOLUME ["/etc/postfix/startup-scripts"]

ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]