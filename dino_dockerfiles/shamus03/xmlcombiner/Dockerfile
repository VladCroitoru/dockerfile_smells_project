FROM microsoft/aspnetcore-build:2 as publish

WORKDIR /src
COPY **/*.csproj ./
RUN ls *.csproj | xargs -n1 dotnet restore \
 && rm -f *.csproj

COPY . .
RUN dotnet publish -c Release -o /publish XmlCombiner.Web

FROM microsoft/aspnetcore:2

COPY --from=publish /publish /app
WORKDIR /app

ENTRYPOINT ["dotnet", "XmlCombiner.Web.dll"]