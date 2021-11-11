# A docker file that upgrades the integration test snapshot. Git diff can help to analyze the differences.
FROM jsii/superchain

WORKDIR /github/workspace
COPY . .
RUN yarn install --check-files --frozen-lockfile
RUN npx projen

CMD [ "npx", "jest", "--passWithNoTests", "--all", "--updateSnapshot" ]
