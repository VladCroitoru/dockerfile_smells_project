#Multistage build
FROM mcr.microsoft.com/dotnet/sdk:5.0 as build
WORKDIR /app
COPY *.sln .
COPY ConversaoPeso.Web/*.csproj ./aspnetapp/
RUN dotnet restore
COPY aspnetapp/. ./aspnetapp/
WORKDIR /app/aspnetapp
RUN dotnet publish -c release -o /published --no-restore

FROM mcr.microsoft.com/dotnet/aspnet:5.0 as rundotnet
WORKDIR /app
COPY --from=build /published ./
EXPOSE 5000
ENTRYPOINT ["dotnet", "aspnetapp.dll"]