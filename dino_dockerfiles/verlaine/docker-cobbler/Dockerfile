FROM ubuntu

RUN apt-get update --fix-missing
RUN apt-get -y install apache2-utils atftpd dnsmasq libapache2-mod-wsgi python-django python-simplejson python-urlgrabber software-properties-common wget iptables pykickstart
RUN wget -qO - http://download.opensuse.org/repositories/home:/libertas-ict:/cobbler26/xUbuntu_14.04/Release.key | apt-key add -
RUN add-apt-repository "deb http://download.opensuse.org/repositories/home:/libertas-ict:/cobbler26/xUbuntu_14.04/ ./"
RUN apt-get update
RUN apt-get -y install cobbler="2.6.5-1"
RUN apt-get autoremove
RUN apt-get autoclean
RUN apt-get clean
RUN cp /etc/apache2/conf.d/cobbler.conf /etc/apache2/conf-available/
RUN cp /etc/apache2/conf.d/cobbler_web.conf /etc/apache2/conf-available/
COPY ./cobbler_patch.conf /etc/apache2/conf-available/cobbler_patch.conf
RUN a2enconf cobbler_patch.conf
RUN chown www-data /var/lib/cobbler/webui_sessions
RUN wget --no-check-certificate https://raw.github.com/jpetazzo/pipework/master/pipework
RUN chmod +x pipework
RUN sed -i '/module = manage_bind/c\module = manage_dnsmasq' /etc/cobbler/modules.conf
RUN sed -i '/module = manage_isc/c\module = manage_dnsmasq' /etc/cobbler/modules.conf
RUN sed -i '/manage_dhcp: 0/c\manage_dhcp: 1' /etc/cobbler/settings
RUN sed -i '/manage_dns: 0/c\manage_dns: 1' /etc/cobbler/settings
RUN rm /etc/dnsmasq.conf
RUN ln -s /etc/cobbler/dnsmasq.template /etc/dnsmasq.conf
RUN a2enconf cobbler cobbler_web
RUN a2enmod proxy proxy_http wsgi
RUN sed -i "s/^SECRET_KEY = .*/SECRET_KEY = '$(openssl rand -hex 16)'/" /usr/share/cobbler/web/settings.py
RUN echo "admin:Cobbler:ec0cff8a86a4bc93ada04ae276f62843" > /etc/cobbler/users.digest
COPY ./import-isos.sh /
COPY ./start.sh /
CMD ["/bin/bash", "/start.sh"]
