# build application
FROM microsoft/dotnet:2.2-sdk AS build
ENV CONFIGURATION=Release
WORKDIR /app
COPY ./app/ ./
RUN dotnet build   --configuration ${CONFIGURATION} \
 && dotnet test    --configuration ${CONFIGURATION} \
 && dotnet publish --configuration ${CONFIGURATION} --output out

# build runtime image
FROM microsoft/dotnet:2.2-aspnetcore-runtime
ENV ASPNETCORE_URLS=http://+:5000
ENV PING=http://localhost:5000/api/health
ENV USER=langbot
ENV GROUP=langbot
ENV UID=2000
ENV GID=2000
ENV HOME=/home/langbot
RUN echo "add ${USER} user" \
 && groupadd --system --gid "${GID}" "${GROUP}" \
 && useradd --system --uid "${UID}" --home-dir "${HOME}" --create-home --gid "${GID}" "${USER}" \
 && echo "install packages" \
 && apt-get --quiet update \
 && apt-get install --yes --no-install-recommends gosu \
 && rm -rf /var/lib/apt/lists/* \
 && echo "install tini" \
 && curl --silent --show-error --location --output /usr/local/bin/tini "https://github.com/krallin/tini/releases/download/v0.18.0/tini-amd64" \
 && echo "12d20136605531b09a2c2dac02ccee85e1b874eb322ef6baf7561cd93f93c855 /usr/local/bin/tini" | sha256sum --check - \
 && chmod +x /usr/local/bin/tini \
 && tini -s true
WORKDIR /app
COPY --from=build /app/web/out ./
COPY scripts /usr/local/bin/
EXPOSE 5000
ENTRYPOINT ["/usr/local/bin/tini", "--"]
CMD ["run-root.sh"]
HEALTHCHECK --interval=60s --timeout=1s CMD run-health.sh || exit 1
