FROM jdeathe/centos-ssh:2.6.1

ARG RELEASE_VERSION="2.3.2"

# ------------------------------------------------------------------------------
# Base install of required packages
# ------------------------------------------------------------------------------
RUN { printf -- \
		'[%s]\nname=%s\nbaseurl=%s\ngpgcheck=%s\nenabled=%s\ngpgkey=%s\n' \
		'mysql57-community' \
		'MySQL 5.7 Community Server' \
		'http://repo.mysql.com/yum/mysql-5.7-community/el/7/$basearch/' \
		'1' \
		'1' \
		'file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql'; \
	} > /etc/yum.repos.d/mysql-community.repo \
	&& rpm --import \
		https://repo.mysql.com/RPM-GPG-KEY-mysql \
	&& yum -y install \
		--setopt=tsflags=nodocs \
		--disableplugin=fastestmirror \
		mysql-community-client-5.7.27-1.el7 \
		mysql-community-common-5.7.27-1.el7 \
		mysql-community-libs-5.7.27-1.el7 \
		mysql-community-server-5.7.27-1.el7 \
		psmisc-22.20-16.el7 \
		sshpass-1.06-2.el7 \
	&& yum versionlock add \
		mysql-community-* \
		psmisc-* \
		sshpass \
	&& rm -rf /var/cache/yum/* \
	&& yum clean all

# ------------------------------------------------------------------------------
# Copy files into place
# ------------------------------------------------------------------------------
ADD src /

# ------------------------------------------------------------------------------
# Provisioning
# - Replace placeholders with values in systemd service unit template
# - Set permissions
# ------------------------------------------------------------------------------
RUN sed -i \
		-e "s~{{RELEASE_VERSION}}~${RELEASE_VERSION}~g" \
		/etc/systemd/system/centos-ssh-mysql@.service \
	&& chmod 600 \
		/etc/my.cnf \
	&& chmod 644 \
		/etc/supervisord.d/{20-mysqld-bootstrap,50-mysqld-wrapper}.conf \
	&& chmod 700 \
		/usr/{bin/healthcheck,sbin/mysqld-{bootstrap,wrapper}}

EXPOSE 3306

# ------------------------------------------------------------------------------
# Set default environment variables
# ------------------------------------------------------------------------------
ENV \
	ENABLE_MYSQLD_BOOTSTRAP="true" \
	ENABLE_MYSQLD_WRAPPER="true" \
	ENABLE_SSHD_BOOTSTRAP="false" \
	ENABLE_SSHD_WRAPPER="false" \
	MYSQL_INIT_LIMIT="10" \
	MYSQL_INIT_SQL="" \
	MYSQL_ROOT_PASSWORD="" \
	MYSQL_ROOT_PASSWORD_HASHED="false" \
	MYSQL_SUBNET="127.0.0.1" \
	MYSQL_USER="" \
	MYSQL_USER_DATABASE="" \
	MYSQL_USER_PASSWORD="" \
	MYSQL_USER_PASSWORD_HASHED="false" \
	SYSTEM_TIMEZONE="UTC"

# ------------------------------------------------------------------------------
# Set image metadata
# ------------------------------------------------------------------------------
LABEL \
	maintainer="James Deathe <james.deathe@gmail.com>" \
	install="docker run \
--rm \
--privileged \
--volume /:/media/root \
jdeathe/centos-ssh-mysql:${RELEASE_VERSION} \
/usr/sbin/scmi install \
--chroot=/media/root \
--name=\${NAME} \
--tag=${RELEASE_VERSION} \
--setopt='--volume {{NAME}}.data-mysql:/var/lib/mysql'" \
	uninstall="docker run \
--rm \
--privileged \
--volume /:/media/root \
jdeathe/centos-ssh-mysql:${RELEASE_VERSION} \
/usr/sbin/scmi uninstall \
--chroot=/media/root \
--name=\${NAME} \
--tag=${RELEASE_VERSION} \
--setopt='--volume {{NAME}}.data-mysql:/var/lib/mysql'" \
	org.deathe.name="centos-ssh-mysql" \
	org.deathe.version="${RELEASE_VERSION}" \
	org.deathe.release="jdeathe/centos-ssh-mysql:${RELEASE_VERSION}" \
	org.deathe.license="MIT" \
	org.deathe.vendor="jdeathe" \
	org.deathe.url="https://github.com/jdeathe/centos-ssh-mysql" \
	org.deathe.description="MySQL 5.7 Community Server - CentOS-7 7.6.1810 x86_64."

HEALTHCHECK \
	--interval=1s \
	--timeout=1s \
	--retries=10 \
	CMD ["/usr/bin/healthcheck"]

CMD ["/usr/bin/supervisord", "--configuration=/etc/supervisord.conf"]
