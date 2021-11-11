FROM mcr.microsoft.com/dotnet/sdk:5.0 as build
WORKDIR /dotnetapp

COPY *.sln .
COPY ConversaoPeso.Web/*.csproj ./ConversaoPeso.Web/
RUN dotnet restore

COPY ConversaoPeso.Web/. ./ConversaoPeso.Web/
WORKDIR /dotnetapp/ConversaoPeso.Web
RUN dotnet publish -c release -o /app --no-restore

FROM mcr.microsoft.com/dotnet/aspnet:5.0
WORKDIR /app
COPY --from=build /app ./
ENTRYPOINT ["dotnet", "ConversaoPeso.Web.dll"]
