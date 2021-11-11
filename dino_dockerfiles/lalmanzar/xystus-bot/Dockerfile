FROM mhart/alpine-node:latest
WORKDIR /app
COPY package.json ./
RUN npm install

FROM mhart/alpine-node:latest
WORKDIR /app
COPY --from=0 /app .
COPY . .
ENV PORT 443
EXPOSE 443
CMD ["npm", "start"]
