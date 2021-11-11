FROM ubuntu:16.04
MAINTAINER Remko Plantenga <sonata82@gmail.com>

# install https support
RUN apt-get update && \
    apt-get -y install apt-transport-https

# add Service Fabric and dotnet repo to apt
RUN echo "deb [arch=amd64] http://apt-mo.trafficmanager.net/repos/servicefabric/ trusty main" > /etc/apt/sources.list.d/servicefabric.list && \
    echo "deb [arch=amd64] https://apt-mo.trafficmanager.net/repos/dotnet-release/ xenial main" > /etc/apt/sources.list.d/dotnetdev.list && \
    echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable" > /etc/apt/sources.list.d/docker.list && \
    apt-key adv --keyserver apt-mo.trafficmanager.net --recv-keys 417A0893 && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 417A0893 && \
    apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net --recv-keys 7EA0A9C3F273FCD8

# update sources
RUN apt-get -y update

# install and set up the SDK for containers and guest executables
RUN echo "servicefabric servicefabric/accepted-eula-v1 select true" | debconf-set-selections && \
    echo "servicefabricsdkcommon servicefabricsdkcommon/accepted-eula-v1 select true" | debconf-set-selections && \
    echo "servicefabricsdkcommon servicefabricsdkcommon/accepted-all-eula select true" | debconf-set-selections
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install servicefabricsdkcommon

ENV USER yeoman

RUN apt-get -y install sudo

# to skip password prompt for sudo users
RUN echo %sudo ALL=NOPASSWD: ALL >> /etc/sudoers

# setting up a user
RUN useradd --create-home --shell /bin/bash $USER && adduser $USER sudo
ENV HOME /home/$USER
WORKDIR $HOME

RUN /opt/microsoft/sdk/servicefabric/common/sdkcommonsetup.sh

# making the $USER owner of node_modules dir to avoid permission errors
RUN chown -R $USER /usr/local/lib/node_modules/

# switching to the non-root user
USER $USER

CMD ["/bin/bash"]