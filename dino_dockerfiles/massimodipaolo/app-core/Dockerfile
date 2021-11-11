FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build-env

# Copy csproj and restore as distinct layers
COPY . /app
WORKDIR /app/samples/web
RUN dotnet restore
RUN dotnet publish -c Release -o out

# App settings
ENV ASPNETCORE_URLS http://*:5000
EXPOSE 5000

# Build runtime image
FROM mcr.microsoft.com/dotnet/core/runtime:3.0
WORKDIR /app/samples/web
COPY --from=build-env /app/samples/web/out .
ENTRYPOINT ["dotnet", "web.dll"]
