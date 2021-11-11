FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src
COPY projectsapi.csproj .
RUN dotnet restore "projectsapi.csproj"
COPY . . 
RUN dotnet publish "projectsapi.csproj" -c Release -o /publish
FROM mcr.microsoft.com/dotnet/sdk:5.0 AS final
WORKDIR /app
COPY --from=build /publish .
ENTRYPOINT [ "dotnet" ]