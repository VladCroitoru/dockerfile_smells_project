FROM jdeathe/centos-ssh:2.6.1

ARG RELEASE_VERSION="2.5.0"

# ------------------------------------------------------------------------------
# Base install of required packages
# ------------------------------------------------------------------------------
RUN { printf -- \
		'[%s]\nname=%s\nbaseurl=%s\nrepo_gpgcheck=%s\ngpgcheck=%s\nenabled=%s\ngpgkey=%s\nsslverify=%s\nsslcacert=%s\nmetadata_expire=%s\n' \
		'varnishcache_varnish63' \
		'varnishcache_varnish63' \
		'https://packagecloud.io/varnishcache/varnish63/el/7/$basearch' \
		'1' \
		'0' \
		'1' \
		'https://packagecloud.io/varnishcache/varnish63/gpgkey' \
		'1' \
		'/etc/pki/tls/certs/ca-bundle.crt' \
		'300'; \
	} > /etc/yum.repos.d/varnishcache_varnish62.repo \
	&& yum -y install \
		--setopt=tsflags=nodocs \
		--disableplugin=fastestmirror \
		gcc-4.8.5-39.el7 \
		varnish-6.3.0-1.el7 \
	&& yum versionlock add \
		varnish \
		gcc \
	&& rm -rf /var/cache/yum/* \
	&& yum clean all

# ------------------------------------------------------------------------------
# Copy files into place
# ------------------------------------------------------------------------------
ADD src /

# ------------------------------------------------------------------------------
# Provisioning
# - Replace placeholders with values in systemd service unit template
# - Create directory for varnishncsa PID file
# - Set permissions
# ------------------------------------------------------------------------------
RUN sed -i \
		-e "s~{{RELEASE_VERSION}}~${RELEASE_VERSION}~g" \
		/etc/systemd/system/centos-ssh-varnish@.service \
	&& mkdir -p \
		/var/{lib/misc,lock/subsys,run}/varnish \
	&& chown \
		varnishlog:varnish \
		/var/{lib/misc,lock/subsys,run}/varnish \
	&& chmod 644 \
		/etc/{supervisord.d/{50-varnishncsa-wrapper,80-varnishd-wrapper}.conf,varnish/docker-default.vcl} \
	&& chmod 700 \
		/usr/{bin/healthcheck,sbin/{varnishd,varnishncsa}-wrapper} \
	&& chmod 750 \
		/usr/sbin/varnishncsa-wrapper \
	&& chgrp varnish \
		/usr/sbin/varnishncsa-wrapper

EXPOSE 80 8443

# ------------------------------------------------------------------------------
# Set default environment variables
# ------------------------------------------------------------------------------
ENV \
	ENABLE_SSHD_BOOTSTRAP="false" \
	ENABLE_SSHD_WRAPPER="false" \
	ENABLE_VARNISHD_WRAPPER="true" \
	ENABLE_VARNISHNCSA_WRAPPER="false" \
	VARNISH_MAX_THREADS="1000" \
	VARNISH_MIN_THREADS="50" \
	VARNISH_OPTIONS="" \
	VARNISH_STORAGE="file,/var/lib/varnish/varnish_storage.bin,1G" \
	VARNISH_THREAD_TIMEOUT="120" \
	VARNISH_TTL="120" \
	VARNISH_VARNISHNCSA_FORMAT="%h %l %u %t \"%r\" %s %b \"%{Referer}i\" \"%{User-agent}i\"" \
	VARNISH_VARNISHNCSA_OPTIONS="" \
	VARNISH_VCL_CONF="/etc/varnish/docker-default.vcl"

# ------------------------------------------------------------------------------
# Set image metadata
# ------------------------------------------------------------------------------
LABEL \
	maintainer="James Deathe <james.deathe@gmail.com>" \
	install="docker run \
--rm \
--privileged \
--volume /:/media/root \
jdeathe/centos-ssh-varnish:${RELEASE_VERSION} \
/usr/sbin/scmi install \
--chroot=/media/root \
--name=\${NAME} \
--tag=${RELEASE_VERSION}" \
	uninstall="docker run \
--rm \
--privileged \
--volume /:/media/root \
jdeathe/centos-ssh-varnish:${RELEASE_VERSION} \
/usr/sbin/scmi uninstall \
--chroot=/media/root \
--name=\${NAME} \
--tag=${RELEASE_VERSION}" \
	org.deathe.name="centos-ssh-varnish" \
	org.deathe.version="${RELEASE_VERSION}" \
	org.deathe.release="jdeathe/centos-ssh-varnish:${RELEASE_VERSION}" \
	org.deathe.license="MIT" \
	org.deathe.vendor="jdeathe" \
	org.deathe.url="https://github.com/jdeathe/centos-ssh-varnish" \
	org.deathe.description="Varnish Cache 6.3 - CentOS-7 7.6.1810 x86_64."

HEALTHCHECK \
	--interval=1s \
	--timeout=1s \
	--retries=5 \
	CMD ["/usr/bin/healthcheck"]

CMD ["/usr/bin/supervisord", "--configuration=/etc/supervisord.conf"]
