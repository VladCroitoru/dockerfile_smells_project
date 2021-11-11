FROM qnib/d-chromium-base

RUN apt-get update && apt-get install -y curl \
 && curl -sL https://deb.nodesource.com/setup_6.x | bash - \
 && apt-get install -y nodejs \
 && npm install -g npm@latest \
 && npm install -g angular-cli yarn
