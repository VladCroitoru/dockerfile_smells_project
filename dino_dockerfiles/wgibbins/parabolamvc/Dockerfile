FROM microsoft/aspnet:1.0.0-beta2

COPY . /app
WORKDIR /app
RUN ["kpm", "restore"]

EXPOSE 5004
ENTRYPOINT ["k", "kestrel"]

