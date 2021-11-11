FROM mcr.microsoft.com/dotnet/sdk:3.1-bionic as build

ARG SME_AE_ENVIRONMENT=dev

ENV AEConnection=$SME_AE_CONNECTION_STRING
ENV EolConnection=$SME_EOL_CONNECTION_STRING
ENV SgpConnection=$SME_SGP_CONNECTION_STRING
ENV CoreSSOConnection=$SME_CORE_SSO_CONNECTION_STRING
ENV SME_AE_JWT_TOKEN_SECRET=$SME_AE_JWT_TOKEN_SECRET
ENV FirebaseToken=$FirebaseToken
ENV FirebaseProjectId=$FirebaseProjectId
ENV ChaveIntegracao=$ChaveIntegracao
ENV SentryDsn=$SentryDsn

ENV TZ=America/Sao_Paulo
ENV DEBIAN_FRONTEND=noninteractive

ADD . /src
WORKDIR /src 

RUN dotnet restore \
    && dotnet build \ 
    && dotnet publish -c Release \   
    && ls -la  /src/src/SME.AE.Api/bin/Release/ \ 
    && cp -R /src/src/SME.AE.Api/bin/Release/netcoreapp3.1/publish /app \ 
    && rm -Rf /src

FROM mcr.microsoft.com/dotnet/aspnet:3.1-bionic as final
COPY --from=build /app /app
WORKDIR /app

RUN apt-get update -y \
    && apt-get install -y tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

EXPOSE 5000-5001
CMD ["/app/SME.AE.Api"]