FROM mcr.microsoft.com/dotnet/runtime:5.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src
COPY ["pTyping.Web/pTyping.Web.csproj", "pTyping.Web/"]
RUN dotnet restore "pTyping.Web/pTyping.Web.csproj"
COPY . .
WORKDIR "/src/pTyping.Web"
RUN dotnet build "pTyping.Web.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "pTyping.Web.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "pTyping.Web.dll"]
EXPOSE 8080/tcp