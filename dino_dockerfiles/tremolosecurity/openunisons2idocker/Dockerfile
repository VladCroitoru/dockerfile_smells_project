FROM centos:7

MAINTAINER Tremolo Security, Inc. - Docker <docker@tremolosecurity.com>

ENV BUILDER_VERSION=1.0 \
    JDK_VERSION=1.8.0 \
    MAVEN_VERSION=3.6.3 \
    OPENUNISON_VERSION="1.0.16"

LABEL name="OpenUnison" \
      vendor="Tremolo Security, Inc." \
      version="1.0.16" \
      release="2019041701" \
### Recommended labels below
      url="https://www.tremolosecurity.com/unison/" \
      summary="Platform for building Tremolo Security OpenUnison" \
      description="OpenUnison is an identity management platforms that can provide solutions for applications and infrastructure. Services include user provisioning, web access management & SSO, LDAP virtual directory and a user self service portal." \
      run='docker run -tdi -p 443:8443 -p 80:8080 -v /tmp/ou/etc:/etc/openunison:Z --name ${NAME} ${IMAGE}' \
      io.k8s.description="Cloud Native Identity Management" \
      io.k8s.display-name="OpenUnison Builder 1.0.16  " \
      io.openshift.expose-services="8080:http,8443:https" \
      io.openshift.tags="identity management,sso,user provisioning,devops,saml,openid connect" \
      io.openshift.tags="builder,1.0.14,sso,identity management" \
      io.openshift.s2i.scripts-url="image:///usr/local/bin/s2i"

RUN yum -y upgrade --security --sec-severity=Important --sec-severity=Critical --setopt=tsflags=nodocs && \
    yum install -y wget unzip which tar java-${JDK_VERSION}-openjdk-devel.x86_64 net-tools.x86_64 && \
    mkdir -p /etc/openunison && \
    mkdir -p /etc/openunison-local && \
    mkdir -p /usr/local/openunison && \
    groupadd -r openunison -g 433 && \
    useradd -u 1001 -r -g openunison -d /usr/local/openunison -s /sbin/nologin -c "OpenUnison Docker image user" openunison && \
    mkdir -p /usr/local/openunison/work && \
    mkdir -p /usr/local/openunison/war && \
    mkdir -p /usr/local/openunison/config && \
    mkdir -p /usr/local/openunison/quartz && \
    mkdir -p /usr/local/openunison/amq && \
    mkdir -p /usr/local/openunison/bin && \
    rm -rf /var/cache/yum

ADD run_openunison.sh /usr/local/openunison/bin/run_openunison.sh
ADD check_alive.py /usr/local/openunison/bin/check_alive.py


# Copy the S2I scripts to /usr/local/bin since I updated the io.openshift.s2i.scripts-url label
COPY ./s2i/bin/ /usr/local/bin/s2i


RUN chown -R 1001:0 \
    /etc/openunison \
    /etc/openunison-local \
    /usr/local/openunison \
  && chmod -R ug+rwX /usr/local/openunison \
  && chmod +x /usr/local/openunison/bin/*


USER 1001

EXPOSE 8080
EXPOSE 8443

CMD ["usage"]
