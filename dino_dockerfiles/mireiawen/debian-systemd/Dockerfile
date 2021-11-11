#
# Debian Systemd image
#
# Based on https://hub.docker.com/r/dramaturg/debian-systemd/
# Using https://github.com/gdraheim/docker-systemctl-replacement

# Debian base image
FROM "debian:9.2"

# Maintainer
MAINTAINER "Mira Liikanen <mir@mireiawen.net>"

# Let the container know that there is no tty
ENV DEBIAN_FRONTEND "noninteractive"

# Let the Systemd know we are inside container
ENV container "docker"

# Install packages
RUN \
	apt-get update && \
	apt-get -y install \
		"aptitude" \
		"apt-utils" \
		"at" \
		"busybox-syslogd" \
		"ca-certificates" \
		"cron" \
		"curl" \
		"dialog" \
		"gnupg" \
		"htop" \
		"initscripts" \
		"iotop" \
		"libncurses5" \
		"libsystemd0" \
		"libudev1" \
		"locales" \
		"logrotate" \
		"lsb-release" \
		"lsof" \
		"openssh-server" \
		"openssl" \
		"postfix" \
		"procps" \
		"screen" \
		"sudo" \
		"systemd" \
		"sysvinit-utils" \
		"udev" \
		"util-linux" \
		"vim" \
		"wget" && \
	aptitude "purge" "~c" && \
	rm -rf \
		"/var/log/apt" \
		"/var/log/dpkg.log" \
		"/var/log/exim4" && \
	mkfifo "/var/spool/postfix/public/pickup"

# Configure the SSH daemon
RUN \
	mkdir -p "/var/run/sshd" && \
	sed -i "s/PermitRootLogin .*/PermitRootLogin without-password/" "/etc/ssh/sshd_config" && \
	touch "/root/.Xauthority"

# Configure the Systemd daemon
# https://github.com/gdraheim/docker-systemctl-replacement
RUN \
	mv "/bin/systemctl" "/bin/systemctl.real"
COPY "systemctl3.py" "/bin/systemctl"
RUN \
	chmod "+x" "/bin/systemctl"

# Clean up some services and targets we are not going to start
RUN \
	cd "/lib/systemd/system/sysinit.target.wants/" && \
	ls | grep -v "systemd-tmpfiles-setup.service" | xargs rm -f && \
	rm -f /lib/systemd/system/sockets.target.wants/*udev* && \
	systemctl.real "mask" -- \
		"tmp.mount" \
		"etc-hostname.mount" \
		"etc-hosts.mount" \
		"etc-resolv.conf.mount" \
		"-.mount" \
		"swap.target" \
		"getty.target" \
		"getty-static.service" \
		"dev-mqueue.mount" \
		"systemd-tmpfiles-setup-dev.service" \
		"systemd-remount-fs.service" \
		"systemd-ask-password-wall.path" \
		"systemd-logind.service" && \
	systemctl.real "set-default" "multi-user.target" && \
	sed -i "s!^#?Storage=.*!Storage=volatile!" "/etc/systemd/journald.conf" && \
	systemctl "enable" "cron.service" && \
	systemctl "enable" "atd.service" && \
	systemctl "enable" "sshd.service"

# Add container boot service
COPY "container-boot.service" "/etc/systemd/system/container-boot.service"
RUN \
	mkdir -p "/etc/container-boot.d" && \
	systemctl "enable" "container-boot.service"

# Configure the logger
COPY "syslog.sh" "/etc/container-boot.d/00-syslog"
RUN \
	chmod "+x" "/etc/container-boot.d/00-syslog"

# Fix the cronjobs
COPY "fix_crontabs.sh" "/etc/container-boot.d/01-fix-crontabs"
RUN \
	chmod "+x" "/etc/container-boot.d/01-fix-crontabs"

# Set up root SSH key
COPY "set_root_pw.sh" "/etc/container-boot.d/99-rootkey"
RUN \
	chmod "+x" "/etc/container-boot.d/99-rootkey"

# Define the entry point
ENTRYPOINT ["/bin/systemctl"]
CMD ["init", "container-boot", "cron", "atd", "sshd"]

# Expose ports
EXPOSE 22
