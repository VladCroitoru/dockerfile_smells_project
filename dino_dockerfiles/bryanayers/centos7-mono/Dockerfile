# Base OS
FROM centos:7

ARG VERSION

# Env setup
ENV HOME /root
ENV VERSION_FULL ${VERSION}-0.xamarin.3.epel7
#WORKDIR /tmp


# Get updates and build deps
RUN \
	yum -y update && \
	yum install -y wget yum-utils && \
	yum clean all && \
	rm -rf /var/cache/yum

# Mono install
#   Notes:
#     mono-data-postgresql unfortunately has been obsoleted by mono-complete, which pulls in 39 MB of dependencies (including mono-data-oracle and devel packages)
RUN \
	rpm --import "http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF" && \
	yum-config-manager --add-repo http://download.mono-project.com/repo/centos/ && \
	yum -y install \
		postgresql \
		libgdiplus0-6.0.5-0.xamarin.1.epel7 \
		mono-core-${VERSION_FULL} \
		mono-data-${VERSION_FULL} \
		mono-data-sqlite-${VERSION_FULL} \
		mono-nunit-${VERSION_FULL} \
		mono-web-${VERSION_FULL} && \
		yum clean all && \
		rm -rf /var/cache/yum
