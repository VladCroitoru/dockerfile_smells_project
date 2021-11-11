#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:3.1 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:3.1 AS build
WORKDIR /src
COPY ["Products/Products.csproj", "Products/"]
COPY ["Contracts/Contracts.csproj", "Contracts/"]
COPY ["Entities/Entities.csproj", "Entities/"]
COPY ["Repository/Repository.csproj", "Repository/"]
COPY ["CurrencyConverter/CurrencyApiConnections.csproj", "CurrencyConverter/"]
RUN dotnet restore "Products/Products.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Products/Products.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Products/Products.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Products.dll"]