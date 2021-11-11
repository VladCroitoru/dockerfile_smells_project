FROM node:14-slim

LABEL name="action-autolabel"
LABEL maintainer="Clay Miller <clay@smockle.com>"
LABEL version="1.0.0"
LABEL repository="https://github.com/smockle/action-autolabel"
LABEL homepage="https://github.com/smockle/action-autolabel"

LABEL com.github.actions.name="Autolabel"
LABEL com.github.actions.description="Label issues based on matched strings."
LABEL com.github.actions.icon="tag"
LABEL com.github.actions.color="blue"

COPY . /action-autolabel
ENTRYPOINT ["node", "--experimental-specifier-resolution=node", "/action-autolabel/dist/index.js"]