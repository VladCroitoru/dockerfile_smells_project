FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src
COPY ["TestWebApi.csproj", "./"]
RUN dotnet restore "TestWebApi.csproj"
COPY . .
WORKDIR "/src/TestWebApi"
RUN dotnet build "TestWebApi.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "TestWebApi.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "TestWebApi.dll"]