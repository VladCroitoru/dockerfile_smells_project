FROM nodesource/trusty

# Add package.json
ADD package.json package.json
RUN npm install --production

# Add all files after npm postinstall completes
ADD . .

ENV NODE_ENV production
EXPOSE 3000

CMD ["npm", "start"]
