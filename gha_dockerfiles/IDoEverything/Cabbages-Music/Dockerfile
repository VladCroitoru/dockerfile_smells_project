# Build it
FROM mcr.microsoft.com/dotnet/sdk:5.0-alpine AS build

WORKDIR /app
COPY ./Cabbage_Music.csproj .
COPY "./nuget.config" .
COPY ./ .
RUN dotnet restore ./Cabbage_Music.csproj

RUN dotnet publish -c Release -o out 

# Run it
FROM mcr.microsoft.com/dotnet/runtime:5.0-alpine AS runtime
WORKDIR /app
COPY --from=build /app/out ./

ENTRYPOINT ["dotnet", "Cabbage_Music.dll"]