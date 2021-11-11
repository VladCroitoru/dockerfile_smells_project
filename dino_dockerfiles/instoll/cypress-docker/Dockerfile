FROM cypress/browsers:chrome63

ENV npm_config_loglevel=warn

RUN npm install -g cypress@1.4.1
RUN cypress verify
RUN cypress --version

CMD ["cypress", "run"]
