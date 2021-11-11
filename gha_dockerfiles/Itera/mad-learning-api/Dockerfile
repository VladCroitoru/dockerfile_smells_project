#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:5.0-buster-slim AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:5.0.102-ca-patch-buster-slim AS build
WORKDIR "/src"
COPY [".editorconfig", "./"]
COPY ["global.json", "./"]
WORKDIR "/src/MadLearning"
COPY ["src/MadLearning/MadLearning.API/MadLearning.API.csproj", "MadLearning.API/"]
COPY ["src/MadLearning/MadLearning.API.Application/MadLearning.API.Application.csproj", "MadLearning.API.Application/"]
COPY ["src/MadLearning/MadLearning.API.Domain/MadLearning.API.Domain.csproj", "MadLearning.API.Domain/"]
COPY ["src/MadLearning/MadLearning.API.Infrastructure/MadLearning.API.Infrastructure.csproj", "MadLearning.API.Infrastructure/"]
RUN dotnet restore "MadLearning.API/MadLearning.API.csproj"
COPY ["./src/*", "."]
WORKDIR "/src/MadLearning/MadLearning.API"
RUN dotnet build "MadLearning.API.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "MadLearning.API.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "MadLearning.API.dll"]