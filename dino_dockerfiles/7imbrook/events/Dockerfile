FROM node:5

WORKDIR /app

# Fetch the dependancies
COPY ./package.json /app/package.json
RUN npm install

# Grab the args
# ARG GOOGLE_CLIENT_ID
ENV GOOGLE_CLIENT_ID=770008175238-ppbq3m2112j68s4f58un50q982m8n6ec.apps.googleusercontent.com
# ARG API_ROOT
ENV API_ROOT=/api/v1/
# ARG NODE_ENV=production
ENV NODE_ENV=development

# Copy in source, this wont copy node_modules because its in the .dockerignore
COPY ./ /app
RUN npm run build

RUN npm install http-server -g

WORKDIR /app/dist
RUN mkdir events
RUN mv * ./events || exit 0
EXPOSE 8000
CMD http-server -p 8000 -a 0.0.0.0 -d false
