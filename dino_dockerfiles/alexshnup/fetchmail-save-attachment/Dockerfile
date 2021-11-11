
# Set the base image to Ubuntu
FROM centos

# File Author / Maintainer
MAINTAINER Aleksei Melnik

RUN yum clean all

# Update the repository
RUN yum -y update

# Install necessary packages
RUN yum install -y fetchmail procmail openssl openssl-perl wget sudo

RUN wget https://mirror.yandex.ru/fedora/linux/releases/25/Everything/x86_64/os/Packages/r/ripmime-1.4.0.9-11.fc24.x86_64.rpm
RUN rpm -Uvh ripmime-1.4.0.9-11.fc24.x86_64.rpm

ADD mailfetcher /mailfetcher
RUN adduser -d /data mailfetcher

RUN chown -R mailfetcher:mailfetcher /data

CMD /mailfetcher/cmd.sh
