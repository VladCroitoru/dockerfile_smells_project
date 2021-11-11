FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
EXPOSE 80
WORKDIR /app
COPY ConversaoPeso.Web/ConversaoPeso.Web.csproj ./ConversaoPeso.Web/
RUN dotnet restore ConversaoPeso.Web/ConversaoPeso.Web.csproj

COPY . .
WORKDIR /app/ConversaoPeso.Web
RUN dotnet publish ConversaoPeso.Web.csproj -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:5.0
WORKDIR /app
COPY --from=build /app/publish .
ENTRYPOINT ["dotnet", "ConversaoPeso.Web.dll"]
