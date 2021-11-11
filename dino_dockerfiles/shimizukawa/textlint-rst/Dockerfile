FROM shimizukawa/textlint

RUN npm install -g textlint-plugin-rst

RUN apk add --no-cache python3 py3-pip \
    && pip3 install docutils-ast-writer
