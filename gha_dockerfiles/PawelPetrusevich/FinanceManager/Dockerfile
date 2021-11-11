#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src
COPY ["FinanceManager/FinanceManager.csproj", "FinanceManager/"]
COPY ["FinanceManager.Identity/FinanceManager.Identity.csproj", "FinanceManager.Identity/"]
COPY ["FinanceManager.Persistence/FinanceManager.Persistence.csproj", "FinanceManager.Persistence/"]
COPY ["FinanceManager.Application/FinanceManager.Application.csproj", "FinanceManager.Application/"]
COPY ["FinanceManager.Domain/FinanceManager.Domain.csproj", "FinanceManager.Domain/"]
COPY ["FinanceManager.Infrastructure/FinanceManager.Infrastructure.csproj", "FinanceManager.Infrastructure/"]
RUN dotnet restore "FinanceManager/FinanceManager.csproj"
COPY . .
WORKDIR "/src/FinanceManager"
RUN dotnet build "FinanceManager.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "FinanceManager.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "FinanceManager.dll"]