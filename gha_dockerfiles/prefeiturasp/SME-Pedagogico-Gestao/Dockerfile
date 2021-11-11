FROM mcr.microsoft.com/dotnet/core/aspnet:2.2-stretch-slim AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/core/sdk:2.2-stretch AS build

RUN wget https://nodejs.org/dist/v8.17.0/node-v8.17.0-linux-x64.tar.gz \ 
    && tar -xzf node-v8.17.0-linux-x64.tar.gz \ 
    && ln -s /node-v8.17.0-linux-x64/bin/node /usr/bin/node \ 
    && ln -s /node-v8.17.0-linux-x64/bin/npm /usr/bin/npm \ 
    && ln -s /node-v8.17.0-linux-x64/bin/npx /usr/bin/npx

WORKDIR /src

COPY ["SME.Pedagogico.Gestao.Aplicacao/SME.Pedagogico.Gestao.Aplicacao.csproj", "/SME.Pedagogico.Gestao.Aplicacao/"]
COPY ["SME.Pedagogico.Gestao.Data/SME.Pedagogico.Gestao.Data.csproj", "/SME.Pedagogico.Gestao.Data/"]
COPY ["SME.Pedagogico.Gestao.Models/SME.Pedagogico.Gestao.Models.csproj", "SME.Pedagogico.Gestao.Models/"]
COPY ["SME.Pedagogico.Gestao.Dominio/SME.Pedagogico.Gestao.Dominio.csproj", "SME.Pedagogico.Gestao.Dominio/"]
COPY ["SME.Pedagogico.Gestao.Infra/SME.Pedagogico.Gestao.Infra.csproj", "SME.Pedagogico.Gestao.Infra/"]
COPY ["SME.Pedagogico.Gestao.IoC/SME.Pedagogico.Gestao.IoC.csproj", "SME.Pedagogico.Gestao.IoC/"]
COPY ["SME.Pedagogico.Gestao.WebApp/SME.Pedagogico.Gestao.WebApp.csproj", "SME.Pedagogico.Gestao.WebApp/"]

RUN dotnet restore "SME.Pedagogico.Gestao.WebApp/SME.Pedagogico.Gestao.WebApp.csproj"

COPY . .

WORKDIR "/src/SME.Pedagogico.Gestao.WebApp"
RUN dotnet build "SME.Pedagogico.Gestao.WebApp.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "SME.Pedagogico.Gestao.WebApp.csproj" -c Release -o /app/publish

RUN mkdir /app/publish/ClientApp/ \
    && mkdir /app/publish/ClientApp/build

RUN cd ClientApp \
     && npm i \
     && npm run build \ 
     && cd .. \
     && mv ClientApp/build /app/publish/ClientApp \     
     && cp SME.Pedagogico.Gestao.WebApp.xml /app/publish/SME.Pedagogico.Gestao.WebApp.xml 


FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
RUN apt-get update && apt-get upgrade -y && update-ca-certificates --fresh
ENTRYPOINT ["dotnet", "SME.Pedagogico.Gestao.WebApp.dll"]


