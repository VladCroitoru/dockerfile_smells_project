FROM microsoft/aspnet:1.0.0-beta4

COPY . /app

WORKDIR /app

RUN ["dnu", "restore"]

ENTRYPOINT ["dnx", ".", "run"]
