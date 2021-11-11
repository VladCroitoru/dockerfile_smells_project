# syntax=docker/dockerfile:1.3
ARG SERVICE_PORT=3002
ARG SERVICE_URL="http://+:${SERVICE_PORT}"
ARG SERVICE_ENV=Development
ARG SERVICE_BUILD_PLAN

FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base
ARG SERVICE_PORT
ENV SERVICE_PORT=${SERVICE_PORT}
WORKDIR /service
EXPOSE $SERVICE_PORT

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
ARG SERVICE_BUILD_PLAN
ENV SERVICE_BUILD_PLAN=${SERVICE_BUILD_PLAN}

WORKDIR /src
COPY ./Api/Api.csproj ./Api/Api.csproj
COPY ./Core/Core.csproj ./Core/Core.csproj
COPY ./Infrastructure/Infrastructure.csproj ./Infrastructure/Infrastructure.csproj
RUN dotnet restore "./Api/Api.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "./Api/Api.csproj" -c $SERVICE_BUILD_PLAN -o /service/build

FROM build AS publish
ARG SERVICE_BUILD_PLAN
ENV SERVICE_BUILD_PLAN=${SERVICE_BUILD_PLAN}

RUN dotnet publish "./Api/Api.csproj" -c $SERVICE_BUILD_PLAN -o /service/publish

FROM base AS final
ARG SERVICE_URL
ENV SERVICE_URL=${SERVICE_URL}

WORKDIR /service

COPY --from=publish /service/publish .

ENV ASPNETCORE_URLS $SERVICE_URL
ENV ASPNETCORE_URLS $SERVICE_URL
ARG SERVICE_ENV
ENV ASPNETCORE_ENVIRONMENT=${SERVICE_ENV}

COPY ./docker/.${SERVICE_ENV}.env .env

ENTRYPOINT dotnet Api.dll