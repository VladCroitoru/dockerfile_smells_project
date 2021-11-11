FROM cypress/base
WORKDIR /tests
ADD . /tests
RUN npm install
RUN $(npm bin)/cypress verify
ENTRYPOINT [ "/tests/entry-point.sh" ]