FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src
COPY ["ConversaoPeso.Web/ConversaoPeso.Web.csproj", "ConversaoPeso.Web/"]
RUN dotnet restore "ConversaoPeso.Web/ConversaoPeso.Web.csproj"
COPY . .
WORKDIR "/src/ConversaoPeso.Web"
RUN dotnet build "ConversaoPeso.Web.csproj" -c release -o /app/build

FROM build AS publish
RUN dotnet publish "ConversaoPeso.Web.csproj" -c release -o /app/publish

FROM base as FINAL
WORKDIR /app
COPY --from=publish /app/publish .
CMD [ "dotnet", "ConversaoPeso.Web.dll" ]