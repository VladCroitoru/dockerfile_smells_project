# First Stage
FROM microsoft/dotnet:2.2-sdk

RUN dotnet tool install -g Microsoft.Web.LibraryManager.Cli
ENV PATH="$PATH:/root/.dotnet/tools"

RUN mkdir /build
WORKDIR /build

COPY src/Hops/ .
RUN libman restore
RUN dotnet restore

RUN dotnet publish -c Release -o out

# Second Stage
FROM microsoft/dotnet:2.2-aspnetcore-runtime

WORKDIR /app
COPY --from=0 /build/out .
COPY --from=0 /build/wwwroot/lib lib

ENV ASPNETCORE_URLS http://+:5000 
EXPOSE 5000/tcp
ENV YourlsApiKey=token
ENTRYPOINT dotnet Hops.dll