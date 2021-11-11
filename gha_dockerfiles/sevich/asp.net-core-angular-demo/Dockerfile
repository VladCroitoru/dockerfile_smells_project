#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base
# Setup NodeJs
RUN apt-get update
RUN apt-get -y install curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs
RUN npm install @angular/cli -g
# End setup

WORKDIR /app
EXPOSE 80
EXPOSE 443

WORKDIR /app
COPY /ClientApp .
RUN npm install
RUN npm rebuild node-sass
RUN npm run build -- --prod

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src
COPY ["angular.csproj", "./"]
RUN dotnet restore "angular.csproj"
COPY . .
WORKDIR "/src/"
RUN dotnet build "angular.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "angular.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
COPY --from=client /app/dist ClientApp/dist
ENTRYPOINT ["dotnet", "angular.dll"]