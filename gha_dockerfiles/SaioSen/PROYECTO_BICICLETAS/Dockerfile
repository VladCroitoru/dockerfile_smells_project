FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build-env
WORKDIR /app

COPY *.csproj ./
RUN dotnet restore

COPY . ./
RUN dotnet publish -c Release -o out

FROM mcr.microsoft.com/dotnet/aspnet:5.0
WORKDIR /app
COPY --from=build-env /app/out .

#CAMBIAR AQUI EL NOMBRE DEL APLICATIVO
#nombre de tu app busca en bin\Release\netcore5.0\plantitas.exe
ENV APP_NET_CORE PROYECTO_BICICLETAS.dll 

CMD ASPNETCORE_URLS=http://*:$PORT dotnet $APP_NET_CORE