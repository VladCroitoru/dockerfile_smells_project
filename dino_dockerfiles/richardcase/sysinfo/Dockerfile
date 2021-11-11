FROM mhart/alpine-node:latest

WORKDIR /src

#COPY src/package.json .
COPY src/. .
RUN npm install

# Add the rest of the source files
#COPY src/. .
EXPOSE 80
CMD ["npm", "start"]
