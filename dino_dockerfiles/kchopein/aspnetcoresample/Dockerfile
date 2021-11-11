FROM microsoft/dotnet:1.0-runtime

WORKDIR /dotnetapp

# copy project.json and restore as distinct layers
# COPY project.json .
# RUN dotnet restore

EXPOSE 5000/tcp
ENV ASPNETCORE_URLS http://*:5000

# copy and build everything else
# COPY . .
# RUN dotnet publish -c Release -o out

# ENTRYPOINT ["dotnet","out/aspnetcoresample.dll"]

COPY out .
ENTRYPOINT ["dotnet","aspnetcoresample.dll"]

