FROM nodesource/trusty:0.12.0

ADD package.json package.json
RUN npm install
ADD . .

CMD ["node", "transip-dyndns.js"]
