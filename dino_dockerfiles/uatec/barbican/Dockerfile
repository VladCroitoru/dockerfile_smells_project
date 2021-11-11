FROM microsoft/dotnet:2-sdk-jessie

RUN mkdir /app
WORKDIR /app
ADD ./src/barbican/barbican.csproj /app/src/barbican/barbican.csproj
RUN dotnet restore ./src/barbican/barbican.csproj
ADD . /app
RUN dotnet publish ./src/barbican -o /app/out

FROM microsoft/dotnet:2-sdk-jessie
RUN mkdir /app
COPY --from=0 /app/out /app
WORKDIR /app

ENV ASPNETCORE_URLS=http://0.0.0.0:5000

CMD dotnet barbican.dll