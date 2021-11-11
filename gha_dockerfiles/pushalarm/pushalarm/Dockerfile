FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["src/PushAlarm/PushAlarm.fsproj", "PushAlarm/"]
RUN dotnet restore "src/PushAlarm/PushAlarm.fsproj"
COPY . .
WORKDIR "/src/PushAlarm"
RUN dotnet build "PushAlarm.fsproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "PushAlarm.fsproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "PushAlarm.dll"]
