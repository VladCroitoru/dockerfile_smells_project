# Use Base Image playwright:bionic
FROM mcr.microsoft.com/playwright:bionic
USER root
WORKDIR /automation
COPY package.json ./
COPY package-lock.json ./
# Install Playwright dependancies
RUN npm ci

COPY . ./

# Install dependencies.
RUN apt-get update
RUN apt-get install wget

# Install Chrome.
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update
RUN apt-get install -y google-chrome-stable

RUN npx playwright install chrome
# Run Tests
RUN npx playwright test TC001_crossbrowsers.spec.js --config=docker.config.js --project=DesktopChromium