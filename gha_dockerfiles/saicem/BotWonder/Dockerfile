#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src
COPY ["BotWonder/BotWonder.csproj", "BotWonder/"]
COPY ["YukinoshitaBot/YukinoshitaBot.csproj", "YukinoshitaBot/"]
RUN dotnet restore "BotWonder/BotWonder.csproj"
COPY . .
WORKDIR "/src/BotWonder"
RUN dotnet build "BotWonder.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "BotWonder.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENV ASPNETCORE_ENVIRONMENT=Production
ENTRYPOINT ["dotnet", "BotWonder.dll"]