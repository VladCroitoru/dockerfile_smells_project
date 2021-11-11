FROM mcr.microsoft.com/dotnet/sdk:5.0.103-alpine3.12 AS build-env
WORKDIR /app
COPY ConversaoPeso.Web/*.csproj ./
RUN dotnet restore 
COPY . ./
RUN dotnet publish ./ConversaoPeso.sln -c Release -o out

FROM mcr.microsoft.com/dotnet/aspnet:5.0-alpine3.12
WORKDIR /app
COPY --from=build-env /app/out .
EXPOSE 80
ENTRYPOINT [ "dotnet", "ConversaoPeso.Web.dll" ]
