FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY mvc080518.csproj ./
RUN dotnet restore mvc080518.csproj
COPY . .
WORKDIR /src/
RUN dotnet build mvc080518.csproj -c Release -o /app

FROM build AS publish
RUN dotnet publish mvc080518.csproj -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "mvc080518.dll"]
