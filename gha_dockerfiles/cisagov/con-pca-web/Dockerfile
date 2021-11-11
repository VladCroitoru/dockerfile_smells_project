ARG VERSION=unspecified

# Stage 1 - Build
FROM node:16-alpine as node

# Set working directory
WORKDIR /app

# Install dependencies
RUN npm install -g npm@latest
RUN npm install -g @angular/cli

# Install Packages
COPY ./src/AdminUI/package*.json ./
RUN npm install

# Copy source
COPY ./src/AdminUI .

# Build project
RUN ng build --configuration production --output-path /app/dist/angular-docker/

# Stage 2 - Run
FROM nginx:1.21.3

# Set Env
ARG VERSION
ENV VERSION=${VERSION}

# Set labels
LABEL org.opencontainers.image.vendor="Cybersecurity and Infrastructure Security Agency"
LABEL org.opencontainers.image.version=${VERSION}

# Copy distribution from build
COPY --from=node /app/dist/angular-docker /usr/share/nginx/html

# Copy nginx configuration
COPY ./etc/default.conf /etc/nginx/conf.d/default.conf
COPY ./etc/mime.types /etc/nginx/mime.types

# Copy entrypoint
COPY ./etc/entrypoint.sh /usr/share/nginx/entrypoint.sh
RUN chmod 755 /usr/share/nginx/entrypoint.sh

# Set entrypoint
ENTRYPOINT ["/usr/share/nginx/entrypoint.sh"]
