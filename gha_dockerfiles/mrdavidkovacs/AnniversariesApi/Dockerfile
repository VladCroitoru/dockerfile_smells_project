FROM mcr.microsoft.com/dotnet/sdk:5.0 AS buildapi
ENV NODE_VERSION=14.17.6
ENV NVM_DIR=/root/.nvm
ENV DOTNET_EnableDiagnostics=0
#RUN type apt-get
RUN apt-get update && apt-get install -y curl libatomic1 python build-essential && mkdir -p $NVM_DIR
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
RUN . "$NVM_DIR/nvm.sh" && nvm install ${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm use v${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm alias default v${NODE_VERSION}
ENV PATH="${NVM_DIR}/versions/node/v${NODE_VERSION}/bin/:${PATH}"
#RUN echo $PATH 
#RUN ls -lah ${NVM_DIR}/versions/node/v${NODE_VERSION}/bin
RUN node --version && npm --version
COPY . /src
WORKDIR /src
RUN (cd Anniversaries.Web && npm install && npm run build)
RUN dotnet publish -c Release -o /src/publish

FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base
LABEL org.opencontainers.image.source https://github.com/mrdavidkovacs/AnniversariesApi
COPY --from=buildapi /src/publish /App
WORKDIR /App
ENV DOTNET_EnableDiagnostics=0
EXPOSE 80
ENV ASPNETCORE_URLS=http://+:80
ENTRYPOINT ["dotnet", "Anniversaries.Api.dll"]