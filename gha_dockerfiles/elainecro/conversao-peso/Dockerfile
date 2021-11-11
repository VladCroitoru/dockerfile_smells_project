FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src
COPY ["ConversaoPeso.Web/ConversaoPeso.Web.csproj", "."]
RUN dotnet restore "./ConversaoPeso.Web.csproj"

COPY ["ConversaoPeso.Web/.", "."] 
WORKDIR "/src/."
RUN dotnet build "ConversaoPeso.Web.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "ConversaoPeso.Web.csproj" -c Release -o /app/publish

FROM base as final
WORKDIR /app
COPY --from=publish /app/publish .
ENV DOTNET_EnableDiagnostics=0
ENTRYPOINT ["dotnet", "ConversaoPeso.Web.dll"]