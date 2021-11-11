FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80
ENV SYNCFUSION_LICENSE_KEY=""
ENV SPELLCHECK_DICTIONARY_PATH=""
ENV SPELLCHECK_JSON_FILENAME=""
FROM microsoft/dotnet:2.1-sdk AS build

WORKDIR /source
COPY ["src/ej2-documenteditor-server/ej2-documenteditor-server.csproj", "./ej2-documenteditor-server/ej2-documenteditor-server.csproj"]
COPY ["src/ej2-documenteditor-server/NuGet.Config", "./ej2-documenteditor-server/"]
RUN dotnet restore "./ej2-documenteditor-server/ej2-documenteditor-server.csproj"
COPY . .
WORKDIR "/source/src"
RUN dotnet build -c Release -o /app

FROM build AS publish
RUN dotnet publish -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "ej2-documenteditor-server.dll"]