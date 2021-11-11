FROM clojure:openjdk-8-tools-deps-1.10.3.998 as build
WORKDIR /app
RUN apt-get install -y curl \
  && curl -sL https://deb.nodesource.com/setup_17.x | bash - \
  && apt-get install -y nodejs \
  && curl -L https://www.npmjs.com/install.sh | sh
COPY deps.edn /app/
COPY package.json /app/
COPY run.sh /app/
COPY ./ /app/
RUN npm install
RUN npm run release app
RUN clojure -T:build uber

FROM openjdk:11
WORKDIR /app
COPY --from=build /app/target/ /app/
COPY --from=build /app/run.sh /app/run.sh
ENV PORT=4000
ENV DATABASE_PORT="$DATABASE_PORT"
ENV DATABASE_USER="$DATABASE_USER"
ENV DATABASE_PASSWORD="$DATABASE_PASSWORD"
ENV DATABASE_NAME="$DATABASE_NAME"
ENV DATABASE_HOST="$DATABSE_HOST"
CMD ["sh", "run.sh"]
