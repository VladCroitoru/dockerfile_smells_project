FROM mcr.microsoft.com/dotnet/sdk:5.0.100
LABEL maintainer="dennis@dhedegaard.dk"
ARG DEBIAN_FRONTEND=noninteractive
EXPOSE 5000
ENV ASPNETCORE_URLS=http://127.0.0.1:5000
ENV FETCHER_HUB_CONNECTION_URL=http://127.0.0.1:5000/data

# Restore .dotnet core packages.
WORKDIR /source
COPY backend/Core/*.csproj ./Core/
COPY backend/Web/*.csproj ./Web/
COPY backend/Web.Tests/*.csproj ./Web.Tests/
COPY backend/Fetcher/*.csproj ./Fetcher/
COPY backend/Poetracker.sln ./
RUN dotnet restore

# Copy everything in.
WORKDIR /source
COPY backend/. .

# Build the web.
WORKDIR /source/Web
RUN dotnet publish --output /app --configuration Release

# Run the published application.
WORKDIR /app
CMD ["dotnet", "Web.dll", "-c", "Release"]
