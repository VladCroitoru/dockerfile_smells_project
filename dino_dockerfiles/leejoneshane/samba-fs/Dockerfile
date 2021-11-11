FROM alpine

ENV SAMBA_ADMIN_PASSWORD S@mba

ADD entrypoint.sh /usr/sbin/
ADD smb.conf /etc/samba/smb.conf
ADD samba.schema /etc/openldap/schema/samba.schema
ADD samba.ldif /etc/openldap/schema/samba.ldif
ADD slapd.conf /etc/openldap/slapd.conf
ADD initldap.ldif /etc/openldap/initldap.ldif

RUN apk update \
    && apk --no-cache --no-progress add bash git sudo zip acl attr make imagemagick \
                                        samba openldap-clients openldap openldap-back-mdb \
                                        perl perl-app-cpanminus perl-ldap perl-mojolicious perl-locale-maketext-lexicon \
    && adduser -G wheel -D -h /mnt -s /bin/bash admin \
    && echo "wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/wheel \
    && chmod 0440 /etc/sudoers.d/wheel \
    && chmod +x /usr/sbin/entrypoint.sh \
    && mkdir -p /root/web && git clone https://github.com/leejoneshane/WAM.git /root/web \
    && mkdir -p /root/etc && cp -Rp /etc /root/etc \
    && mkdir /web && cp -Rp /root/web/. /web

EXPOSE 137/udp 138/udp 139 445 8080
VOLUME ["/mnt", "/etc", "/web"]
ENTRYPOINT ["entrypoint.sh"]
