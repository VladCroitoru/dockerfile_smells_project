# FunderMaps Ecosystem

# Build application solution
FROM mcr.microsoft.com/dotnet/sdk AS build
WORKDIR /source

# The subtool must be defined. The build container will only build the
# subtool application.
ARG subtool

RUN test -n "$subtool" || (echo "subtool argument not set" && false)

# Copy the entire solution in the container
COPY . .

# Print the application version in the source
RUN find . -type f -exec sed -i "s/@@VERSION@@/$(git describe --long --always)/" {} + \
    && find . -type f -exec sed -i "s/@@COMMIT@@/$(git rev-parse HEAD)/" {} +

# Publish and configure subtool application
WORKDIR "/source/src/$subtool"
RUN dotnet publish -c release -o /app \
    && git describe --long --always > /app/VERSION \
    && git rev-parse HEAD > /app/COMMIT \
    && echo "$subtool" > /app/SUBTOOL \
    && ln -s "$subtool" /app/entry \
    && rm -f /app/appsettings.json /app/appsettings.*.json \
    && cp /source/contrib/etc/_appsettings.Production.json /app/appsettings.Production.json \
    && cp /source/contrib/etc/_appsettings.Staging.json /app/appsettings.Staging.json

# Build runtime image
FROM mcr.microsoft.com/dotnet/aspnet
ENV DOTNET_PRINT_TELEMETRY_MESSAGE=false
WORKDIR /app
COPY --from=build /app .
RUN if grep -Fxq  "FunderMaps.BatchNode" SUBTOOL ; then \
  apt -y update; \
  apt -y install gdal-bin; \
fi
EXPOSE 80/tcp
ENTRYPOINT "/app/entry"
