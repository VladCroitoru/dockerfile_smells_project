# sdk required to build ASP.NET app
FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /source


COPY *.sln .
COPY OsmIntegrator/*.csproj ./OsmIntegrator/

COPY OsmIntegrator/. ./OsmIntegrator/
RUN cd OsmIntegrator \ 
    && dotnet add package Microsoft.EntityFrameworkCore.Analyzers --version 5.0.4 \
    && dotnet publish -c release -o /dist --no-restore

# runtime environment for ASP.NET
FROM mcr.microsoft.com/dotnet/aspnet:5.0
WORKDIR /app
COPY --from=build /dist ./
ENTRYPOINT ["dotnet", "osmintegrator.dll"]
