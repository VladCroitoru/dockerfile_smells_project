FROM node:16.10.0-alpine3.14
RUN addgroup app && adduser -S -G app app && mkdir /app && chown app:app /app
USER app
WORKDIR /app
RUN mkdir data
COPY --chown=app:app package*.json .
RUN npm install
COPY --chown=app:app . .
ENV API_URL=http://test.com
EXPOSE 3000
CMD ["npm", "start"]