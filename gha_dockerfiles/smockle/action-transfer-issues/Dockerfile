FROM node:14-slim

LABEL name="action-transfer-issues"
LABEL maintainer="Clay Miller <clay@smockle.com>"
LABEL version="1.0.0"
LABEL repository="https://github.com/smockle/action-transfer-issues"
LABEL homepage="https://github.com/smockle/action-transfer-issues"

LABEL com.github.actions.name="Transfer Issues"
LABEL com.github.actions.description="Transfer issues from one repo to another, even across orgs."
LABEL com.github.actions.icon="copy"
LABEL com.github.actions.color="blue"

COPY . /action-transfer-issues
ENTRYPOINT ["node", "--experimental-specifier-resolution=node", "/action-transfer-issues/dist/index.js"]