FROM debian:stretch
LABEL maintainer="Timothée Eid <timothee.eid@erizo.fr>"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        apache2 \
        modsecurity-crs \
        libapache2-mod-security2 \
    && rm -r /var/lib/apt/lists/*

# Add default apache conf
ADD conf/apache/apache2.conf /etc/apache2/apache2.conf
ADD conf/apache/security2.conf /etc/apache2/mods-available/security2.conf

# Add the WAF conf
ENV MODSEC_SecRuleEngine="DetectionOnly"
RUN cat /etc/modsecurity/modsecurity.conf-recommended \
    | sed 's#^SecRuleEngine .*#SecRuleEngine ${MODSEC_SecRuleEngine}#g' \
    | sed 's#^SecAuditLog .*#SecAuditLog /dev/stdout#g' \
    | sed 's#^SecDataDir .*#SecDataDir /run/apache2/modsecurity/data#g' \
    | sed 's#^SecTmpDir .*#SecTmpDir /run/apache2/modsecurity/tmp#g' \
    | sed 's#^SecAuditEngine .*#SecAuditEngine Off#g' \
    > /etc/modsecurity/modsecurity.conf
RUN mkdir /etc/modsecurity/rules.pre
RUN mkdir /etc/modsecurity/rules.post

# Create the runtime volume
RUN mkdir -p /run/apache2
RUN chown -R www-data:www-data /run/apache2
VOLUME /run/apache2
VOLUME /tmp

# Site volume
RUN rm /etc/apache2/sites-enabled/*
ADD conf/apache/default-site.conf /etc/apache2/sites-enabled/default.conf
VOLUME /etc/apache2/sites-enabled/

EXPOSE 80
EXPOSE 443

# Add the start script
ADD run.sh /run.sh
RUN chmod 500 /run.sh
CMD [ "/run.sh" ]
