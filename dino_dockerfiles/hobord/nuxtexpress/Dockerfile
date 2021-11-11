FROM node:8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app/
#RUN git clone https://github.com/hobord/nuxtexpress.git .
RUN npm install

# Build
RUN npm run build 

# Test app
#RUN npm run test:unit && npm run test:e2e

#ENV HOST 0.0.0.0
EXPOSE 3000

#ENTRYPOINT [ "npm", "run", "test" ]
CMD [ "npm", "start" ]
#CMD [ "bash" ]