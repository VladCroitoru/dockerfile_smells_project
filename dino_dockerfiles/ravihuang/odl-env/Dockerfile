#######################################################
# This dockerfile builds a opendaylight develop       #
# environment                                         #
#                                                     #
# Author:Ravi Huang                                   #
# Repository: ravihuang/odl-env                       #
# Version: 1.0                                        #
#                                                     #
#######################################################

FROM ravihuang/maven

MAINTAINER Ravi Huang 1657231876@qq.com


##### Update system and install apps
RUN     yum -y update && \
        rpm --import "http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF" && \
        yum-config-manager --add-repo http://download.mono-project.com/repo/centos/  
        
RUN     yum install -y wget git zip bzip2 \
        make binutils gcc gcc-c++ boost-devel openssl-devel perl-ExtUtils-MakeMaker \
        unixODBC-devel gtest-devel redhat-lsb-core json-c-devel libcurl-devel \
        perl-Digest-SHA tomcat-native graphviz --nogpgcheck            
  
##### Environment
ENV     MVN_SETTING_URL     https://raw.githubusercontent.com/opendaylight/odlparent/master/settings.xml
ENV     MAVEN_OPTS          "-Xmx1024m -XX:MaxMetaspaceSize=512m"

##### Maven setting
RUN     mkdir $HOME/.m2 && \
        wget -q -O - $MVN_SETTING_URL > ~/.m2/settings.xml

##### Expose port for controller
# EXPOSE  6633 8181

##### Sync source code folder
VOLUME  ["/home/odl"]
VOLUME  ["/root/.m2/repository"]

##### Clean
RUN     yum clean all
RUN     rm -rf /tmp/* /var/tmp/*
