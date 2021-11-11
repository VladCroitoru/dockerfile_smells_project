FROM mcr.microsoft.com/dotnet/runtime:5.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src
COPY ["RunHelloWorld.csproj", "RunHelloWorld/"]
RUN dotnet restore "RunHelloWorld/RunHelloWorld.csproj"
COPY . .
WORKDIR "/src/RunHelloWorld"
RUN dotnet build "RunHelloWorld.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "RunHelloWorld.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "RunHelloWorld.dll"]
