FROM mcr.microsoft.com/dotnet/sdk:5.0.202-alpine3.13-amd64 AS build
WORKDIR /app

# Copy csproj and restore as distinct layers
COPY src/Exercism.TestRunner.CSharp/Exercism.TestRunner.CSharp.csproj ./
RUN dotnet restore -r linux-musl-x64

# Copy everything else and build
COPY src/Exercism.TestRunner.CSharp/ ./
RUN dotnet publish -r linux-musl-x64 -c Release -o /opt/test-runner --no-restore --self-contained true

# Build runtime image
FROM mcr.microsoft.com/dotnet/runtime-deps:5.0.5-alpine3.13-amd64 AS runtime

# Enable globalization as some exercises use it
ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=false
RUN apk add --no-cache icu-libs tzdata

WORKDIR /opt/test-runner

COPY --from=build /opt/test-runner/ .
COPY --from=build /usr/local/bin/ /usr/local/bin/

COPY run.sh /opt/test-runner/bin/

ENTRYPOINT ["sh", "/opt/test-runner/bin/run.sh"]
