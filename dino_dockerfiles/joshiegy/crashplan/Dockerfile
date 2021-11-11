FROM centos:7
MAINTAINER Joshi Friberg

#COPY ./CrashPlan_4.5.0_Linux.tgz /CrashPlan_4.5.0_Linux.tgz

RUN mkdir /config && mkdir /crashplan
COPY ./linker.sh /crashplan/linker.sh
COPY ./entrypoint.sh /crashplan/entrypoint.sh

VOLUME ["/config", "/media"]

#RUN yum -y update && \
RUN yum -y install \
grep \
sed \
cpio \
gzip \
coreutils \
which

COPY ./custom-install.sh /install.sh
RUN curl -o /CrashPlan.tgz https://download1.code42.com/installs/linux/install/CrashPlan/CrashPlan_4.5.2_Linux.tgz && \
tar xpzf /CrashPlan.tgz -C /opt/ && \
rm -rf /CrashPlan.tgz &&\
mv /install.sh /opt/crashplan-install/install.sh && \
cd /opt/crashplan-install && \
bash ./install.sh && \
rm -rf /opt/crashplan-install && \
chmod a+x /crashplan/linker.sh /crashplan/entrypoint.sh &&\
sed -i 's/nice\ -n\ 19\ \$JAVACOMMON\ \$SRV_JAVA_OPTS\ -classpath\ \$FULL_CP\ com\.backup42\.service\.CPService.*/nice -n 19 $JAVACOMMON $SRV_JAVA_OPTS -classpath $FULL_CP com.backup42.service.CPService/' /crashplan/crashplan/bin/CrashPlanEngine

EXPOSE 4242/tcp 4243/tcp

ENTRYPOINT /crashplan/entrypoint.sh
