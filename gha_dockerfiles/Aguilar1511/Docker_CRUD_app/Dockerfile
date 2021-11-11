FROM node:latest
WORKDIR /app
COPY . /app

ARG NODE_ENV
RUN if [ "$NODE_ENV" = "development" ]; \       
        then npm install; \ 
        else npm install --only=production; \
        fi
        
ENV PORT 5000
CMD ["node", "app.js"]

