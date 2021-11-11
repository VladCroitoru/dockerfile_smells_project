FROM java:8-jre

MAINTAINER Benjamin Stein <ben-st@diffus.org>

# the user jd2 will run with and his group
ARG user=jd2
ARG group=jd2
ARG uid=943
ARG gid=943

# install paxctl
RUN apt-get update
RUN apt-get install -yq  paxctl \
    && rm -rf /var/lib/apt/lists

# add specified user and group and create and chown the install and downloads dir
RUN groupadd -g ${gid} ${group} \
	&& useradd -u ${uid} -g ${gid} -m -s /bin/bash ${user} \
	&& mkdir -p /opt/JDownloader/ /opt/downloads \
	&& chown -R ${uid}:${group} /opt/JDownloader/ /opt/downloads


# (permanent change, by converting the binary headers PT_GNU_STACK into PT_PAX_FLAGS)
# m: Disable MPROTECT // grsec: denied RWX mmap of <anonymous mapping>
RUN paxctl -c -v -m /usr/bin/java

# copy the start script to the Container
COPY startJD2.sh /opt/JDownloader/
# make it executable
RUN chmod +x /opt/JDownloader/startJD2.sh

# switch to the specified user
USER ${user}

# download the jdownloader jar file and run it to create the neccesary files and folders
RUN \
	wget -O /opt/JDownloader/JDownloader.jar --user-agent="https://hub.docker.com/r/ben-st/jdownloader2-headless/" --progress=bar:force http://installer.jdownloader.org/JDownloader.jar && \
	java -Djava.awt.headless=true -jar /opt/JDownloader/JDownloader.jar ;


# Run this when the container is started
CMD /opt/JDownloader/startJD2.sh
