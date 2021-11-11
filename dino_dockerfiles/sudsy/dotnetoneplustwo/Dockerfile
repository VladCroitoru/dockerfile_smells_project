FROM microsoft/dotnet:1.0-runtime

#add ms registry for .net core 2.0

RUN apt-get update

RUN apt-get -y install curl libunwind8 gettext apt-transport-https

RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg

RUN mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg

RUN sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-debian-jessie-prod jessie main" > /etc/apt/sources.list.d/dotnetdev.list'

RUN apt-get update

RUN apt-get -y install dotnet-sdk-2.0.0
 
