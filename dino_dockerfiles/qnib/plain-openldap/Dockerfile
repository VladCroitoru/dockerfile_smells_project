# inspired by https://github.com/larrycai/docker-openldap
# it is based on https://github.com/rackerlabs/dockerstack/blob/master/keystone/openldap/Dockerfile
# also the files/more.ldif from http://www.zytrax.com/books/ldap/ch14/#ldapsearch
FROM qnib/uplain-init:14.04

# install slapd in noninteractive mode
RUN apt-get update \
 && apt-get install -y nmap \
 && echo 'slapd/root_password password password' | debconf-set-selections \
 && echo 'slapd/root_password_again password password' | debconf-set-selections \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y slapd ldap-utils \
 && rm -rf /var/lib/apt/lists/*

COPY opt/qnib/lapd/bin/start.sh /opt/qnib/ldap/bin/
CMD ["/opt/qnib/ldap/bin/start.sh"]
