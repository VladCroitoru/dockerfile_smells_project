FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build-env
WORKDIR /src
COPY *.sln .
COPY ConversaoPeso.Web/. ./ConversaoPeso.Web/
WORKDIR /src/ConversaoPeso.Web
RUN dotnet publish -c release -o /app --no-restore

FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS runtime
WORKDIR /app
COPY --from=build-env /app ./
ENTRYPOINT ["dotnet", "ConversaoPeso.Web.dll"]
