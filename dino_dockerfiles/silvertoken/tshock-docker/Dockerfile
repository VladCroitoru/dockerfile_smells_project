FROM centos:latest

MAINTAINER silvertoken <1569232+silvertoken@users.noreply.github.com>

# Add mono repository
# Update and install mono
RUN yum install -y \
		yum-utils \
		epel-release \
		unzip \
		wget && \
	rpm --import "http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF" && \
	yum-config-manager --add-repo "http://download.mono-project.com/repo/centos/" && \
	yum -y update && \
	yum -y install mono-complete && \
	yum clean all

#Copy start script
COPY start.sh /start

# Download and install TShock
ENV TSHOCK_VERSION=4.3.25

RUN mkdir /world /config /logs /plugins /tshock && \
	cd /tshock && \
	wget https://github.com/NyxStudios/TShock/releases/download/v$TSHOCK_VERSION/tshock_$TSHOCK_VERSION.zip && \
	unzip tshock_$TSHOCK_VERSION.zip && \
	rm tshock_$TSHOCK_VERSION.zip && \
	chmod +x /tshock/TerrariaServer.exe && \
	chmod +x /start

# Allow for external data
VOLUME ["/world", "/logs", "/config" "/plugins"]

# Set working directory to server
WORKDIR /tshock

# run the server
ENTRYPOINT [ "/start" ]