FROM	ubuntu:xenial

ENV DEBCONF_NONINTERACTIVE_SEEN="true" \
    DEBIAN_FRONTEND="noninteractive"

RUN		apt-get update -qq \
			&& apt-get install -yqq samba smbclient libcap2-bin \
			&& apt-get clean \
	    && rm -rf /var/lib/apt/lists/*

COPY src/smb.conf /etc/samba/smb.conf
COPY src/entrypoint.sh /opt/entrypoint.sh

RUN chmod 0755 /opt/entrypoint.sh \
		&& chmod 0644 /etc/samba/smb.conf \
		&& mkdir -m 0755 /etc/samba/conf.d/

HEALTHCHECK --interval=60s --timeout=15s CMD smbclient -L 'localhost' -U 'guest' -m SMB3

EXPOSE 137/udp 138/udp 139 445

ENTRYPOINT ["/opt/entrypoint.sh"]
