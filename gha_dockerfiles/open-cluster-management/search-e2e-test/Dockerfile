# Copyright (c) 2020 Red Hat, Inc.

FROM mikefarah/yq:4 as builder
FROM cypress/included:8.5.0 as production

USER root

COPY --from=builder /usr/bin/yq /usr/local/bin/yq

COPY package.json .
COPY package-lock.json .
COPY cypress.json .
COPY jest.config.js .
COPY start-tests.sh .
COPY download-clis.sh .
COPY config ./config
COPY tests ./tests
COPY build/rbac-setup.sh .
COPY build/rbac-clean.sh .
RUN npm i

RUN sh download-clis.sh

RUN ["chmod", "+x", "start-tests.sh"]

ENTRYPOINT ["./start-tests.sh"]
