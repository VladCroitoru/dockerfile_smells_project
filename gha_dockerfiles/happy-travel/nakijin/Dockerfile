FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base

ARG VAULT_TOKEN
ARG BUILD_VERSION
ARG CONSUL_HTTP_TOKEN

ENV BUILD_VERSION=$BUILD_VERSION
ENV HTDC_VAULT_TOKEN=$VAULT_TOKEN
ENV CONSUL_HTTP_TOKEN=$CONSUL_HTTP_TOKEN

WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:5.0-focal  AS build
ARG GITHUB_TOKEN
WORKDIR /src
COPY *.sln ./
COPY . .
RUN dotnet restore
WORKDIR /src/HappyTravel.Nakijin.Api
RUN dotnet build -c Release -o /app

FROM build AS publish
RUN dotnet publish -c Release -o /app

FROM base AS final
WORKDIR /app

COPY --from=publish /app .

HEALTHCHECK --interval=6s --timeout=10s --retries=3 CMD curl -sS 127.0.0.1/health || exit 1

ENTRYPOINT ["dotnet", "HappyTravel.Nakijin.Api.dll"]
