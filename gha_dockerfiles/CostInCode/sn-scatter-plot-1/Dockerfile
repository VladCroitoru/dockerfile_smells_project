FROM circleci/node:16.7-browsers

USER root

RUN apt-get install -y google-chrome-stable

COPY package.json yarn.lock ./

RUN yarn install --frozen-lockfile

COPY . .

RUN yarn build

CMD ["sh","-c","DocId=$(curl -s --data-binary @data/apps/Executive_Dashboard.qvf http://localhost:9076/v1/apps/import | jq -r '.attributes.id') && APP_ID=$DocId && npx aw puppet --glob 'test/**/*.spec.js' --mocha.bail false --mocha.timeout 10000"]



