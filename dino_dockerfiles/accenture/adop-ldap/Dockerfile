FROM dinkel/openldap:2.4.40

MAINTAINER Darren Jackson, <darren.a.jackson>

# Replicate all default environment variables from the base image and customize the needed one's. 
# This is to be able to use a custom entrypoint and perform all needed settings

ENV INITIAL_ADMIN_USER admin.user
ENV INITIAL_ADMIN_PASSWORD="" GITLAB_PASSWORD="" JENKINS_PASSWORD=""
ENV SLAPD_PASSWORD=""
ENV SLAPD_DOMAIN ldap.example.com
ENV SLAPD_FULL_DOMAIN "dc=ldap,dc=example,dc=com"
ENV SLAPD_LDIF_BASE="/var/tmp/ldifs"
ENV SLAPD_LOAD_LDIFS=""

# End environment variable definition

# Copy in configuration files
COPY resources/modules/ppolicy.ldif /etc/ldap.dist/modules/ppolicy.ldif

COPY resources/configuration/check_password.conf /etc/ldap.dist/check_password.conf

COPY resources/ldap_init.sh /usr/local/bin/
RUN chmod u+x /usr/local/bin/ldap_init.sh

COPY resources/load_ldif.sh /usr/local/bin/
RUN chmod u+x /usr/local/bin/load_ldif.sh

COPY resources/ldifs /var/tmp/ldifs

COPY resources/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod u+x /usr/local/bin/entrypoint.sh

# Install ldap utility commands
RUN cp -a /etc/ldap.dist/* /etc/ldap && \
apt-get update && \
DEBIAN_FRONTEND=noninteractive apt-get install -y ldap-utils wget gcc make libdb-dev && \
apt-get clean && rm -rf /var/lib/apt/lists/*

# Get openldap source to compile check password
RUN wget -O /root/openldap-2.4.40.tgz https://www.openldap.org/software/download/OpenLDAP/openldap-release/openldap-2.4.40.tgz && \
	cd /root && \
	tar -zxvf openldap-2.4.40.tgz &&  \
	cd openldap-2.4.40 && ./configure && \
	make depend

RUN wget -O /root/cracklib-2.9.6.tar.gz https://github.com/cracklib/cracklib/releases/download/cracklib-2.9.6/cracklib-2.9.6.tar.gz && \
	cd /root && gunzip cracklib-2.9.6.tar.gz && tar -xvf cracklib-2.9.6.tar && \
	cd cracklib-2.9.6 && ./configure --prefix=/usr --disable-static  --with-default-dict=/lib/cracklib/pw_dict && \
	make && make install

RUN wget -O /root/cracklib-words-2.9.6.gz https://github.com/cracklib/cracklib/releases/download/cracklib-2.9.6/cracklib-words-2.9.6.gz && \
        install -v -m644 -D /root/cracklib-words-2.9.6.gz /usr/share/dict/cracklib-words.gz && \
	gunzip -v /usr/share/dict/cracklib-words.gz && \
	ln -v -sf cracklib-words /usr/share/dict/words && install -v -m755 -d /lib/cracklib &&\
        create-cracklib-dict /usr/share/dict/cracklib-words

RUN wget -O /root/openldap-ppolicy-check-password-1.1.tar.gz https://github.com/ltb-project/openldap-ppolicy-check-password/archive/v1.1.tar.gz && \
	cd /root && gunzip openldap-ppolicy-check-password-1.1.tar.gz && tar -xvf openldap-ppolicy-check-password-1.1.tar && \
	cd openldap-ppolicy-check-password-1.1 && \
	make install  CONFIG="/etc/ldap/check_password.conf" LDAP_INC="-I/root/openldap-2.4.40/include/ -I/root/openldap-2.4.40/servers/slapd" \
	CRACKLIB="/lib/cracklib/" CRACKLIB_LIB="/usr/lib/libcrack.so.2" LIBDIR="/usr/lib/ldap/"

# Cleanup
RUN DEBIAN_FRONTEND=noninteractive apt-get remove -y wget gcc libdb-dev make && rm -rf /root/*

# Override entry point
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["slapd", "-d", "32768", "-u", "openldap", "-g", "openldap"]
