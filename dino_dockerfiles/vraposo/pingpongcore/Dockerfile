FROM microsoft/dotnet:1.0-sdk-projectjson

RUN mkdir app
WORKDIR app

# copy project.json and restore
COPY src/pingpongcore/project.json .
RUN dotnet restore

# copy everything else and build it
COPY src/pingpongcore/ .
RUN dotnet publish -c Release -o out

ENTRYPOINT ["dotnet", "out/pingpongcore.dll"]

# set up network
ENV ASPNETCORE_URLS=http://+:5000
EXPOSE 5000
