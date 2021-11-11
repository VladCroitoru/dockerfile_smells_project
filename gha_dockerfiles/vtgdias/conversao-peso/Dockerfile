FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /app
COPY *.sln .
COPY ConversaoPeso.Web/*.csproj ./ConversaoPeso.Web/
RUN dotnet restore

COPY ConversaoPeso.Web/. ./ConversaoPeso.Web/
WORKDIR /app/ConversaoPeso.Web
RUN dotnet publish -c release -o /published --no-restore
RUN ls -lah


FROM mcr.microsoft.com/dotnet/aspnet:5.0
WORKDIR /app
COPY --from=build /published ./
EXPOSE 80
ENTRYPOINT ["dotnet", "ConversaoPeso.Web.dll"]