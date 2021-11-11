FROM ascdc/apache2-php56
MAINTAINER ASCDC <asdc.sinica@gmail.com>

ADD run.sh /run.sh

RUN \
	chmod +x /*.sh && \
	apt-get update && apt-get install -y libapache2-modsecurity libapache2-mod-fastcgi && \
	mv /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf && \
	sed -i 's/SecRuleEngine DetectionOnly/SecRuleEngine On/g' /etc/modsecurity/modsecurity.conf && \
	sed -i 's/SecResponseBodyAccess On/SecResponseBodyAccess Off/g' /etc/modsecurity/modsecurity.conf && \
	sed -i 's/<\/IfModule>/Include "\/usr\/share\/modsecurity-crs\/*.conf"\nInclude "\/usr\/share\/modsecurity-crs\/activated_rules\/*.conf"\n<\/IfModule>/g' /etc/apache2/mods-enabled/security2.conf && \
	ln -s /usr/share/modsecurity-crs/base_rules/modsecurity_crs_41_sql_injection_attacks.conf /usr/share/modsecurity-crs/activated_rules/

EXPOSE 80
WORKDIR /var/www/html
ENTRYPOINT ["/run.sh"]