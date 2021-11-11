 #Base Image built from most current Java version OFFICIAL
FROM java:openjdk-9-b149-jre

 #Install Prereqs
RUN apt-get update \
    && apt-get -qy --no-install-recommends install \
        cpio \
        curl \
        sed \
        wget \
    && apt-get -q -y clean \
    && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* \
    && rm -rf /usr/share/man/?? /usr/share/man/??_*

 #Configuring ports and setting up Data Volumes
EXPOSE 4282 4283 4285 4286
VOLUME ["/var/log/proserver”,”/var/opt/proserver”,”/opt/proserver”]

 #Copying proserver.sh install and start script
 #Crashplan downlaods for the first time
COPY ./proserver.sh /
RUN chmod +x /proserver.sh
ENTRYPOINT ["/proserver.sh"]
