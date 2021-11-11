# Azure Commander Dockerfile
ARG ubuntu_version=18.04

FROM ubuntu:$ubuntu_version
MAINTAINER <herve leclerc> herve.leclerc@alterway.fr
#
# This image install azure-cli, ansible, and powershell to drive efficiently azure 
#  Un commentaire pour demo

ARG POWERSHELL_RELEASE=v6.1.3

ARG POWERSHELL_PACKAGE=powershell_6.1.3-1.ubuntu.18.04_amd64.deb
ARG POWERSHELL_HOME="/opt/microsoft/powershell/$POWERSHELL_RELEASE"

RUN apt-get update                                  && \
    apt-get install -y software-properties-common   && \
    apt-add-repository -y ppa:ansible/ansible       && \
    apt-get install -y --no-install-recommends         \
                       build-essential                 \
                       nodejs                          \
                       python-dev                      \
                       python-pip                      \
                       libxml2-dev                     \
                       libxslt-dev                     \
                       libssl-dev                      \
                       libffi-dev                      \
                       ansible                         \
                       libc6                           \
                       libcurl3                        \
                       ca-certificates                 \
                       libgcc1                         \
                       libicu60                        \
                       libssl1.0.0                     \
                       libstdc++6                      \
                       libtinfo5                       \
                       libunwind8                      \
                       libuuid1                        \
                       zlib1g                          
RUN apt-get install -y libcurl4                        \
                        node-gyp                       \   
                        npm                            \
                        curl                           \
                        git                         


# Azure cli
RUN curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | tee /etc/apt/trusted.gpg.d/microsoft.asc.gpg > /dev/null
RUN export AZ_REPO=$(lsb_release -cs) && echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | tee /etc/apt/sources.list.d/azure-cli.list
RUN apt-get update && apt-get -y install azure-cli        

RUN pip install --upgrade pip
RUN pip install -U setuptools         && \              
    pip install --upgrade ansible     && \               
    pip install azure==4.0.0                       

 
RUN apt-get install -y liblttng-ust0
# Install PowerShell package and clean up
RUN curl -SLO https://github.com/PowerShell/PowerShell/releases/download/$POWERSHELL_RELEASE/$POWERSHELL_PACKAGE \
    && dpkg -i $POWERSHELL_PACKAGE \
    && rm $POWERSHELL_PACKAGE

ENV PSHOME "$POWERSHELL_HOME"

RUN pwsh -Command Install-Package -Force -Name AzureRM.NetCore -Source https://www.powershellgallery.com/api/v2 -ProviderName NuGet -ExcludeVersion -Destination $POWERSHELL_HOME/Modules


RUN apt-get clean -y && apt-get autoclean -y

CMD ["/bin/bash"]
