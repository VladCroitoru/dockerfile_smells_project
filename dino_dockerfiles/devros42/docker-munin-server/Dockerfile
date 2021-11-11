FROM ubuntu:bionic

MAINTAINER git@shaf.net

ENV ALLOWED_HOSTS="127.0.0.1/32" \
	HOSTNAME="unRAID" \
	TZ="America/New_York"

RUN \
	apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get install -y munin munin-libvirt-plugins munin-node munin-plugins-core munin-plugins-extra apache2 lm-sensors smartmontools sysstat git tzdata && \
	git clone https://github.com/scanterog/munin-plugin-docker.git && \
	chmod 775 munin-plugin-docker/docker_* && \
	cp munin-plugin-docker/docker_* /etc/munin/plugins/ && \
	apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* && \
	sed -ri 's/^log_file.*/# \0/; \
			s/^pid_file.*/# \0/; \
			s/^background 1$/background 0/; \
			s/^setsid 1$/setsid 0/; \
			' /etc/munin/munin-node.conf && \
	/bin/echo -e "cidr_allow ${ALLOWED_HOSTS}" >> /etc/munin/munin-node.conf && \
	ln -s /usr/share/munin/plugins/sensors_   /etc/munin/plugins/sensors_temp && \
	ln -s /usr/share/munin/plugins/sensors_   /etc/munin/plugins/sensors_fan && \
	ln -s /usr/share/munin/plugins/sensors_   /etc/munin/plugins/sensors_volt && \
	ln -s /usr/share/munin/plugins/hddtemp_smartctl   /etc/munin/plugins/hddtemp_smartctl && \
	ln -s /usr/share/munin/plugins/iostat   /etc/munin/plugins/iostat && \
	ln -s /usr/share/munin/plugins/meminfo   /etc/munin/plugins/meminfo && \
	mkdir /var/run/munin  && \
	chown munin:munin /var/run/munin

ADD start.sh /
ADD payload/apache24.conf /etc/munin/

EXPOSE 80 4949

# Define data volumes
VOLUME ["/etc/munin/munin-conf.d", "/var/cache/munin/www", "/var/lib/munin"]

CMD ["/start.sh"]
