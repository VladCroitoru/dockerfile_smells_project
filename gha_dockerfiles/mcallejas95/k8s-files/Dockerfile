FROM jenkins/jenkins:latest

USER root

# requisitos docker
RUN apt-get update \
    && apt-get -y install sudo \
        apt-transport-https \
        ca-certificates \
        curl \
        software-properties-common \
        wget

# docker repos
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
    && echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable" >> /etc/apt/sources.list.d/additional-repositories.list \
    && echo "deb http://ftp-stud.hs-esslingen.de/ubuntu xenial main restricted universe multiverse" >> /etc/apt/sources.list.d/official-package-repositories.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 437D05B5 \
    && apt-get update

#RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - \
#    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable" \
#    apt-get update \
#    apt-cache policy docker-ce

# docker
RUN apt-get -y install docker-ce

# docker-compose
RUN curl -L https://github.com/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose

# agregar al grupo de docker
#RUN usermod -aG docker $USER
#USER jenkins

###Requisitos para pipelines

#JAVA / FIREFOX
RUN apt-get update \
    && apt-get -y install \
       openjdk-8-jdk \
       firefox-esr \
       git

# NETCORE 5.0
RUN wget https://packages.microsoft.com/config/ubuntu/21.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN rm packages-microsoft-prod.deb
RUN apt-get install -y apt-transport-https && \ 
    apt-get update && \ 
    apt-get install -y dotnet-sdk-5.0

# NODE
#RUN curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
#RUN bash nodesource_setup.sh
#RUN apt install nodejs

RUN apt-get update -y \
    && apt-get -y install curl gnupg ca-certificates \
    && curl -L https://deb.nodesource.com/setup_12.x | bash \
    && apt-get update -y \
    && apt-get install -y \
        nodejs

#SSH 
RUN apt update && apt install -y \
    openssh-server -y \
    sshpass
RUN service ssh start

#ANDROID SDK
RUN wget https://dl.google.com/android/repository/commandlinetools-linux-7583922_latest.zip
RUN unzip commandlinetools-linux-7583922_latest.zip
RUN rm commandlinetools-linux-7583922_latest.zip
RUN mkdir -p android-sdk/cmdline-tools/tools/ 
RUN cp -a cmdline-tools/. android-sdk/cmdline-tools/tools/
RUN export ANDROID_SDK_ROOT=/android-sdk 
RUN yes | /android-sdk/cmdline-tools/tools/bin/./sdkmanager --licenses

#Login GIT
RUN git config --global user.name "InActionSaaS" \
    && git config --global user.email "jm.islas@dataware.com.mx"

#dotnet sonarscanner
RUN dotnet tool install --global dotnet-sonarscanner
RUN export PATH="$PATH:$HOME/.dotnet/tools"