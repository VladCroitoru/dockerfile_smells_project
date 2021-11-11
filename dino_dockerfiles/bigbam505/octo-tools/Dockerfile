FROM microsoft/dotnet:1.0-runtime
MAINTAINER brent@bmontague.com

WORKDIR /octo

RUN curl -o OctopusTools.tar.gz https://download.octopusdeploy.com/octopus-tools/4.14.1/OctopusTools.4.14.1.portable.tar.gz && tar -xvzf OctopusTools.tar.gz && rm OctopusTools.tar.gz

ENTRYPOINT [ "dotnet", "Octo.dll" ]
CMD [ "help" ]
