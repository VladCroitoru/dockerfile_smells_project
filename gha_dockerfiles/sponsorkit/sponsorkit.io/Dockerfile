FROM mcr.microsoft.com/dotnet/aspnet:5.0-buster-slim AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build-dotnet
WORKDIR /
COPY ["src/api/Sponsorkit.csproj", "src/api/"]
RUN dotnet tool restore
RUN dotnet restore "src/api/Sponsorkit.csproj"
COPY . .
RUN dotnet build "src/api/Sponsorkit.csproj" -c Release -o /app/build

FROM build-dotnet AS publish-dotnet
RUN dotnet publish "src/api/Sponsorkit.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish-dotnet /app/publish .
ENTRYPOINT ["dotnet", "Sponsorkit.dll"]