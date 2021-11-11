FROM microsoft/dotnet:2.0.3-sdk as builder
COPY . /build
WORKDIR /build

RUN dotnet restore
RUN dotnet publish --output ../out/ --configuration Release MotionTelegramConnector

FROM microsoft/aspnetcore:2.0.3
WORKDIR /app
COPY --from=builder /build/out .

ARG CONTAINER_PORT=5000
ARG ASPNETCORE_URLS=http://+:$CONTAINER_PORT

ENV ASPNETCORE_URLS $ASPNETCORE_URLS

EXPOSE $CONTAINER_PORT/tcp

ADD run.sh .

ENTRYPOINT ["/app/run.sh"]
