FROM microsoft/dotnet:latest
COPY . /app
WORKDIR /app
 
VOLUME /docs

RUN dotnet restore
RUN dotnet build
 
EXPOSE 5000/tcp
ENV ASPNETCORE_URLS http://*:5000
ENV ASPNETCORE_ENVIRONMENT Development
 
ENTRYPOINT dotnet run