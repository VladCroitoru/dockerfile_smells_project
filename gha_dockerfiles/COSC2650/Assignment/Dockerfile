# Build runtime image
FROM mcr.microsoft.com/dotnet/aspnet:5.0

# New Relic licence key
ENV NEW_RELIC_LICENCE_KEY=""
ENV NEW_RELIC_API_KEY=""
ENV NEW_RELIC_ACCOUNT_ID=""
ENV CONNECTION_STRING=""
ENV CORS_URLS=""

# Install the NewRelic agent
RUN apt-get update \
        && apt-get upgrade -y \
        && apt-get install -y wget ca-certificates gnupg \
        && echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | tee /etc/apt/sources.list.d/newrelic.list \
        && wget https://download.newrelic.com/548C16BF.gpg \
        && apt-key add 548C16BF.gpg \
        && apt-get update \
        && apt-get install -y newrelic-netcore20-agent \
        && rm -rf /var/lib/apt/lists/* \
        && if [ ! -d ./API ]; then mkdir -p ./API; fi 

# Enable the NewRelic agent
ENV CORECLR_ENABLE_PROFILING=1 \
CORECLR_PROFILER={36032161-FFC0-4B61-B559-F6C5D41BAE5A} \
CORECLR_NEWRELIC_HOME=/usr/local/newrelic-netcore20-agent \
CORECLR_PROFILER_PATH=/usr/local/newrelic-netcore20-agent/libNewRelicProfiler.so \
NEW_RELIC_APP_NAME="API"

# Set the working directory and copy thr build assets
COPY out ./API/

# Expose port 80
EXPOSE 80

# Run the app
ENTRYPOINT ["/usr/local/newrelic-netcore20-agent/run.sh", "dotnet /API/API.dll"]
