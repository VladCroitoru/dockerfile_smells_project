FROM node:14-alpine
RUN ln -s /usr/bin/nodejs /usr/bin/node
ADD app /app
RUN cd app && npm install --silent
EXPOSE 5000
WORKDIR /app
COPY app/.env /app/.env
RUN chmod +rwx /app/.env && chmod ugo+rw /app/.env
CMD ["node", "server.js"]