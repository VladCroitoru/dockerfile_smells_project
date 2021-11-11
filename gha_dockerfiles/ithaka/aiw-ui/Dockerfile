# Builds a Docker to deliver dist/
FROM docker.artifactory.acorn.cirrostratus.org/node:11.0
# Add environment variables
ENV PORT=80
ENV SAGOKU=true
# Create app directory
WORKDIR /usr/src/app
# Copy built application files (built by docker-build-image.sh)
COPY dist ./dist
# Copy server package.json for commands and dependencies
COPY server/package.json ./
# Install runtime dependencies
RUN npm install --production
# Host on good ol' 80
EXPOSE 80

CMD [ "npm", "run", "serve:ssr" ]
