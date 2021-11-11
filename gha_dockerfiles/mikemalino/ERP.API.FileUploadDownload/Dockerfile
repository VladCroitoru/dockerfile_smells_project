#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:3.1 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:3.1 AS build
WORKDIR /src
COPY ["nuget.config", "."]
COPY ["API/Notes/Premier.API.FileUploadDownload/Premier.API.FileUploadDownload.csproj", "API/Notes/Premier.API.FileUploadDownload/"]
COPY ["API/CommonData/Premier.CommonData.ERPNA/Premier.CommonData.ERPNA.csproj", "API/CommonData/Premier.CommonData.ERPNA/"]
RUN dotnet restore "API/Notes/Premier.API.FileUploadDownload/Premier.API.FileUploadDownload.csproj"
COPY . .
WORKDIR "/src/API/Notes/Premier.API.FileUploadDownload"
RUN dotnet build "Premier.API.FileUploadDownload.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Premier.API.FileUploadDownload.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Premier.API.FileUploadDownload.dll"]