FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build-env
WORKDIR /app

# Copy csproj and restore as distinct layers
COPY src/TravelBlog/TravelBlog.csproj src/TravelBlog/libman.json ./src/TravelBlog/
RUN set -x \
    && dotnet restore src/TravelBlog/TravelBlog.csproj \
    && dotnet tool install -g Microsoft.Web.LibraryManager.Cli \
    && export PATH="$PATH:/root/.dotnet/tools" \
    && libman restore --root src/TravelBlog

# Copy everything else and build
COPY . ./
RUN dotnet publish --no-restore -c Release -o /app/out src/TravelBlog/TravelBlog.csproj

# Build runtime image
FROM mcr.microsoft.com/dotnet/core/aspnet:3.1
WORKDIR /app
COPY --from=build-env /app/out .
ENTRYPOINT ["dotnet", "TravelBlog.dll"]
