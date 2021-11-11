FROM osixia/light-baseimage:1.3.3-amd64

#########################################
##             SET LABELS              ##
#########################################

# set version and maintainer label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="Version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="Logicwar <logicwar@gmail.com>"


#########################################
##        ENVIRONMENTAL CONFIG         ##
#########################################

# Set default environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    DUID=1001 DGID=1001 \
    JVM_XX_OPTS="-XX:+UseG1GC" \
    JVM_MIN_MEM="1024M" \
    JVM_MAX_MEM="2048M" \
    TYPE="VANILLA" \
    VERSION="LATEST" \
    FORGEVERSION="RECOMMENDED" \
    EULA=""

#########################################
##          DOWNLOAD PACKAGES          ##
#########################################

# Download and install Dependencies
RUN \
 echo "**** Install Dependencies ****" && \
 apt-get update && \
 apt-get install --no-install-recommends -y \
	wget \
	curl \
	jq \
	unzip \
	git && \
 echo "**** cleanup ****" && \
 apt-get clean && \
 rm -rf \
	/var/lib/apt/lists/* \	
	/tmp/* \
	/var/tmp/*


#########################################
##       COPY & RUN SETUP SCRIPT       ##
#########################################
# copy setup, default parameters and init files
COPY service /container/service
COPY defaults /defaults
COPY external_packages /opt

# set permissions and run install-service script
RUN \
 chmod -R +x /container/service && \
 /container/tool/install-service


#########################################
##         EXPORTS AND VOLUMES         ##
#########################################

EXPOSE 25565 25575
VOLUME /opt/minecraft/data

