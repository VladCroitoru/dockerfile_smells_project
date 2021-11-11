#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src
COPY ["MySchool.Api/MySchool.Api.csproj", "MySchool.Api/"]
RUN dotnet restore "MySchool.Api/MySchool.Api.csproj"
COPY . .
WORKDIR "/src/MySchool.Api"
RUN dotnet build "MySchool.Api.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "MySchool.Api.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "MySchool.Api.dll"]