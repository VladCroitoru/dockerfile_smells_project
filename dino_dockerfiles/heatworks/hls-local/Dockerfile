ARG node=node

FROM $node:8

WORKDIR /heatworks-lab-local
ADD src/ src/
ADD package.json package.json
ADD Procfile Procfile
ADD tsconfig.server.json tsconfig.server.json

RUN npm install

EXPOSE 4000
CMD ["npm", "start"]