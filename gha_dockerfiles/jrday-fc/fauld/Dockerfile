FROM node:14-buster-slim@sha256:def3a1529489f23679f8a35e9410709cc3a0b8ae91b6065c7b7807863253990c

WORKDIR /app

COPY package* .
COPY version.txt .
COPY index.js .
RUN npm install

CMD ["node", "index.js"]
