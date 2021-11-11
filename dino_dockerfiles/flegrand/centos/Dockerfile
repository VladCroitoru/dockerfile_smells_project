FROM centos:7

# Install last updates
RUN yum upgrade -y

# Packages
RUN yum install -y zip unzip procps systat net-tools

# Timezone
RUN ln -sf /usr/share/zoneinfo/Europe/Zurich /etc/localtime
