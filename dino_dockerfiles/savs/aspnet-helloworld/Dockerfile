FROM microsoft/aspnet:1.0.0-beta5
COPY . /app
WORKDIR /app
RUN ["dnu", "restore"]

EXPOSE 5004
ENTRYPOINT ["dnx", ".", "kestrel"]