FROM macadmins/sal:2.7.3
MAINTAINER Allister Banks <al@aru-b.com>

ENV SAL_LDAP_SERVER_URI='ldap://ldap' SAL_LDAP_START_TLS=false \
SAL_LDAP_USER_ATTR="sAMAccountName" \
SAL_LDAP_LOGGING=false
RUN apt-get update && apt-get install -y python-setuptools python-dev  libffi-dev libssl-dev libldap2-dev libsasl2-dev \
&& easy_install pip && pip install requests pyOpenSSL ndg-httpsclient pyasn1 django-auth-ldap
ADD settings.py /home/app/sal/sal/settings.py
