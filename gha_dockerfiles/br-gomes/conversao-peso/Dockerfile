FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /app

COPY . ./

RUN dotnet restore
RUN dotnet publish ./ConversaoPeso.Web/ConversaoPeso.Web.csproj -c release -o dist


FROM mcr.microsoft.com/dotnet/aspnet:5.0
WORKDIR /app
COPY --from=build /app/dist ./

EXPOSE 80

ENTRYPOINT ["dotnet", "ConversaoPeso.Web.dll"]