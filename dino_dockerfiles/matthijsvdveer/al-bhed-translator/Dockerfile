FROM node:8.9.1

# Override the base log level (info).
ENV NPM_CONFIG_LOGLEVEL warn

# Install and configure `serve`.
RUN npm install -g serve
CMD serve -s build
EXPOSE 5000

COPY package.json package.json
RUN npm install

# Copy all local files into the image.
COPY . .

# Build for production.
RUN npm run build --production