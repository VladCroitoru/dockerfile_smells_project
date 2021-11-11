FROM node:0.10

RUN npm install -g bower grunt-cli karma superstatic

RUN curl -sLo /usr/local/bin/ep https://github.com/kreuzwerker/envplate/releases/download/v0.0.6/ep-linux && chmod +x /usr/local/bin/ep

WORKDIR /app
EXPOSE 8080

CMD ["/usr/local/bin/ep", "/app/*", "/app/assets/*", "--", "/usr/local/bin/superstatic", "--port","8080","--host","0.0.0.0", "--gzip"]