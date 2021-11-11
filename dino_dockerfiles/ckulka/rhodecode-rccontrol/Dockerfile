FROM centos:7
LABEL maintainer="cyrill.kulka@gmail.com"

ENV RC_INSTALLER    RhodeCode-installer-linux-build20171123_1300
ENV RC_CHECKSUM     e3b702ebc0e98577ed834781c5a2173f1ece37fab084bb05210fcf6234e011c4

# Create the RhodeCode user
RUN useradd rhodecode -u 1000 -s /sbin/nologin				\
		&& mkdir -m 0755 -p /opt/rhodecode /data			\
		&& chown rhodecode:rhodecode /opt/rhodecode /data	\
		&& yum install -y bzip2 postgresql					\
		&& curl -so /usr/local/bin/crudini https://raw.githubusercontent.com/pixelb/crudini/0.9/crudini \
		&& chmod +x /usr/local/bin/crudini

USER rhodecode
WORKDIR /home/rhodecode

# Install RhodeCode Control
RUN curl -so $RC_INSTALLER https://dls-eu.rhodecode.com/dls/NzA2MjdhN2E2ODYxNzY2NzZjNDA2NTc1NjI3MTcyNzA2MjcxNzIyZTcwNjI3YQ==/rhodecode-control/latest-linux-ce \
		&& echo "$RC_CHECKSUM *$RC_INSTALLER" |  sha256sum -c -	\
		&& chmod 755 $RC_INSTALLER								\
		&& ./$RC_INSTALLER --accept-license						\
		&& rm $RC_INSTALLER

# Add additional tools
COPY files .
