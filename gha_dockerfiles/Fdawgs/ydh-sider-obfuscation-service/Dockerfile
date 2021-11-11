FROM node:lts-alpine

# Workdir
WORKDIR /usr/app

# Copy and install packages
COPY . .
# Git is needed to install node modules from GitHub
# Curl needed for healthcheck command
RUN apk add --no-cache curl git && \
    npm ci --ignore-scripts && npm cache clean --force

# Node images provide 'node' unprivileged user to run apps and prevent
# privilege escalation attacks
USER node
CMD ["node", "."]