FROM microsoft/dotnet:runtime
MAINTAINER github@vanefferenonline.nl

ARG OCTO_TOOLS_VERSION=6.13.1

LABEL maintainer="github@vanefferenonline.nl" \ 
	  version=$OCTO_TOOLS_VERSION

WORKDIR /octo

RUN curl -o OctopusTools.tar.gz https://download.octopusdeploy.com/octopus-tools/${OCTO_TOOLS_VERSION}/OctopusTools.${OCTO_TOOLS_VERSION}.portable.tar.gz && tar -xvzf OctopusTools.tar.gz && rm OctopusTools.tar.gz

ENTRYPOINT [ "dotnet", "Octo.dll" ]
CMD [ "help" ]
