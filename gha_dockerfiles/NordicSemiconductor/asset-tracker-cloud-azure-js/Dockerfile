FROM ubuntu:20.04 as base
WORKDIR /workdir

RUN \
    # Update system
    apt-get -y update && \
    apt-get -y upgrade && \
    # Install Node.js
    apt -y install curl dirmngr apt-transport-https lsb-release ca-certificates && \
    /bin/bash -c 'curl -sL https://deb.nodesource.com/setup_14.x | bash -' && \
    apt-get install -y nodejs && \
    node -v && \
    # Azure CLI
    curl -sL https://aka.ms/InstallAzureCLIDeb | bash && \
    az --version && \
    # Azure Functions Core Tools, see https://github.com/Azure/azure-functions-core-tools/blob/dev/README.md#linux
    export DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=true && \
    apt -y install wget && \
    wget -q https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb && \
    rm packages-microsoft-prod.deb && \
    apt-get -y update && \
    apt -y install azure-functions-core-tools-3 && \
    func

RUN \
    # download extension bundle ("func start" will do this otherwise)
    apt-get install -y unzip && \
    wget -q https://functionscdn.azureedge.net/public/ExtensionBundles/Microsoft.Azure.Functions.ExtensionBundle/1.8.1/Microsoft.Azure.Functions.ExtensionBundle.1.8.1_any-any.zip && \
    mkdir -p /root/.azure-functions-core-tools/Functions/ExtensionBundles/Microsoft.Azure.Functions.ExtensionBundle/1.8.1 && \
    unzip Microsoft.Azure.Functions.ExtensionBundle.1.8.1_any-any.zip -d /root/.azure-functions-core-tools/Functions/ExtensionBundles/Microsoft.Azure.Functions.ExtensionBundle/1.8.1 && \
    rm Microsoft.Azure.Functions.ExtensionBundle.1.8.1_any-any.zip

ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=true
ENV FUNCTIONS_CORE_TOOLS_TELEMETRY_OPTOUT=1
ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=true

EXPOSE 7071/tcp
