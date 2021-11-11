# Stage 1
FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /build

# Copy csproj and restore as distinct layers
COPY ApplyToBecomeInternal/ApplyToBecome.Data/ ./ApplyToBecome.Data/
COPY ApplyToBecomeInternal/DocumentGeneration/ ./DocumentGeneration/
COPY ApplyToBecomeInternal/ApplyToBecomeInternal/ ./ApplyToBecomeInternal/

WORKDIR ApplyToBecomeInternal
RUN dotnet restore
RUN dotnet publish -c Release -o /app

# Stage 2
FROM mcr.microsoft.com/dotnet/core/aspnet:3.1 AS final
WORKDIR /app
COPY --from=build /app .
ENTRYPOINT ["dotnet", "ApplyToBecomeInternal.dll"]
