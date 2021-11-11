FROM node:8.10-slim

# Create app directory
RUN mkdir -p /app
WORKDIR /app
ADD . .

RUN yarn --frozen-lockfile 
ENV PORT=3000

EXPOSE 3000
CMD [ "node", "index" ]
