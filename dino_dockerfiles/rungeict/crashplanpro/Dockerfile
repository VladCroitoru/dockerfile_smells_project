FROM centos
#########################################
##        ENVIRONMENTAL CONFIG         ##
#########################################
# Set correct environment variables
ENV CRASHPLAN_VERSION=4.9.0_1436674888490_33

# LC_ALL=en_US.UTF-8"     \
# LANG="en_US.UTF-8"      \
# LANGUAGE="en_US.UTF-8"

#########################################
##         RUN INSTALL SCRIPT          ##
#########################################

RUN yum install -y bash wget ca-certificates openssl tar expect findutils coreutils procps cpio grep which net-tools

RUN mkdir /tmp/crashplan \
  && mkdir -p /usr/local/crashplan/log/


RUN wget -O- https://web-eam-msp.crashplanpro.com/client/installers/CrashPlanPRO_${CRASHPLAN_VERSION}_Linux.tgz \
	| tar -xz --strip-components=1 -C /tmp/crashplan

COPY files/ /

RUN chmod +rx /app/entrypoint.sh /app/crashplan.sh


WORKDIR /tmp/crashplan
COPY crashplan.exp /tmp/crashplan/
RUN chmod +rx /tmp/crashplan/crashplan.exp
RUN expect /tmp/crashplan/crashplan.exp

# Remove unneccessary directories
RUN rm -rf /boot /home /lost+found /media /mnt /run /srv /usr/local/crashplan/log/* /tmp/crashplan

#########################################
##              VOLUMES                ##
#########################################
VOLUME [ "/usr/local/crashplan", "/var/lib/crashplan", "/storage" ]

#########################################
##            EXPOSE PORTS             ##
#########################################
EXPOSE 4243 4242

WORKDIR /usr/local/crashplan

ENTRYPOINT ["/app/entrypoint.sh"]
CMD [ "/app/crashplan.sh" ]
