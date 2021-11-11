FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src
COPY ["Vue.Splash-API/Vue.Splash-API.csproj", "Vue.Splash-API/"]
RUN dotnet restore "Vue.Splash-API/Vue.Splash-API.csproj"
COPY . .
WORKDIR "/src/Vue.Splash-API"
RUN dotnet build "Vue.Splash-API.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Vue.Splash-API.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Vue.Splash-API.dll"]
