FROM zenato/puppeteer

WORKDIR /data

ADD index.* package.json yarn.lock ./
RUN npm install --only=dev && /data/node_modules/.bin/babel ./index.js --out-file ./index.bundle.js
RUN npm install && cp ./node_modules/mermaid/dist/mermaid.min.js .

ADD test ./test
RUN node index.bundle.js -i ./test/flowchart.mmd -o /tmp/test.png; rm /tmp/test.png

ENTRYPOINT ["node", "/data/index.bundle.js"]
CMD ["--help"]
