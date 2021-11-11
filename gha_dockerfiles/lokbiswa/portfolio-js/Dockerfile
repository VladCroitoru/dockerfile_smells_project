FROM node:17-alpine

# ENV vars
ENV REFRESH_TOKEN = ""
ENV EMAIL = ""
ENV CLIENT_SECRET = ""
ENV REDIRECT_URL = ""
ENV CLIENT_ID = ""
ENV AUTH_CODE = ""

WORKDIR /app
COPY . /app/

RUN [ "npm", "install", "--production" ]

EXPOSE 9005

CMD ["node", "./server/server.js"]
