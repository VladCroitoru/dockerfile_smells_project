FROM node:14-slim

LABEL name="action-filter-issues"
LABEL maintainer="Clay Miller <clay@smockle.com>"
LABEL version="1.0.0"
LABEL repository="https://github.com/smockle/action-filter-issues"
LABEL homepage="https://github.com/smockle/action-filter-issues"

LABEL com.github.actions.name="Filter Issues"
LABEL com.github.actions.description="Output a space-delimited list of issues matching the specified criteria."
LABEL com.github.actions.icon="filter"
LABEL com.github.actions.color="blue"

COPY . /action-filter-issues
ENTRYPOINT ["node", "--experimental-specifier-resolution=node", "/action-filter-issues/dist/index.js"]