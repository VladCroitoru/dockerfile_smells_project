# inspired by https://github.com/larrycai/docker-openldap
# it is based on https://github.com/rackerlabs/dockerstack/blob/master/keystone/openldap/Dockerfile
# also the files/more.ldif from http://www.zytrax.com/books/ldap/ch14/#ldapsearch
ARG DOCKER_REGISTRY=docker.io
FROM ${DOCKER_REGISTRY}/qnib/plain-openldap:2.4.21@sha256:4739edebc326064a24bf5c7a1be577bdf5850881bd8154039fb22b925587cf8f

COPY files /ldap

RUN service slapd start \
 && cd /ldap \
 && ldapadd -Y EXTERNAL -H ldapi:/// -f back.ldif \
 && ldapadd -Y EXTERNAL -H ldapi:/// -f sssvlv_load.ldif \
 && ldapadd -Y EXTERNAL -H ldapi:/// -f sssvlv_config.ldif \
 && ldapadd -x -D cn=admin,dc=qnib,dc=inc -w password -c -f front.ldif \
 && ldapadd -x -D cn=admin,dc=qnib,dc=inc -w password -c -f users.ldif
