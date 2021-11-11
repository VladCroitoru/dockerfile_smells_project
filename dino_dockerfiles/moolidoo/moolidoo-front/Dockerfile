FROM node:4
RUN mkdir /moolidoo-front
ADD ./ /moolidoo-front/
WORKDIR /moolidoo-front
RUN npm install --no-optional
EXPOSE 8080
ENTRYPOINT ["npm", "start"]
