FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src
COPY ["FadingFlame/FadingFlame.csproj", "FadingFlame/"]
RUN dotnet restore "FadingFlame/FadingFlame.csproj"
COPY . .
WORKDIR "/src/FadingFlame"
RUN dotnet build "FadingFlame.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "FadingFlame.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "FadingFlame.dll"]
