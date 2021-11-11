FROM mcr.microsoft.com/dotnet/aspnet:5.0-focal AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:5.0-focal AS build
WORKDIR /
COPY ["./ConversaoPeso.Web/ConversaoPeso.Web.csproj", "./ConversaoPeso.Web/"]

RUN dotnet restore "./ConversaoPeso.Web/ConversaoPeso.Web.csproj"

COPY ./ConversaoPeso.Web ./ConversaoPeso.Web

RUN dotnet build "./ConversaoPeso.Web/ConversaoPeso.Web.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "./ConversaoPeso.Web/ConversaoPeso.Web.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "ConversaoPeso.Web.dll"]