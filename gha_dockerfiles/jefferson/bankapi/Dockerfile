#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:3.1 AS build
WORKDIR /src
COPY ["BankApi/BankApi.csproj", "BankApi/"]
COPY ["BankInfrastructure/BankInfrastructure.csproj", "BankInfrastructure/"]
COPY ["BankApplication/BankApplication.csproj", "BankApplication/"]
COPY ["BankDomain/BankDomain.csproj", "BankDomain/"]
RUN dotnet restore "BankApi/BankApi.csproj"
COPY . .
WORKDIR "/src/BankApi"
RUN dotnet build "BankApi.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "BankApi.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .

CMD ASPNETCORE_URLS=http://*:$PORT dotnet BankApi.dll

#ENTRYPOINT ["dotnet", "BankApi.dll"]