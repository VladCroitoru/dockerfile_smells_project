FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src
COPY ["Compass.Security.Web/Compass.Security.Web.csproj", "Compass.Security.Web/"]
RUN dotnet restore "Compass.Security.Web/Compass.Security.Web.csproj"
COPY . .
WORKDIR "/src/Compass.Security.Web"
RUN dotnet build "Compass.Security.Web.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Compass.Security.Web.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
#ENTRYPOINT ["dotnet", "Compass.Security.Web.dll"]
#HEROKU
CMD ASPNETCORE_URLS=http://*:$PORT dotnet Compass.Security.Web.dll

