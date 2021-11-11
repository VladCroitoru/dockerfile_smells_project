FROM samdoshi/haskell-stack
ADD . /tmp/rss-dummy-backend
WORKDIR /tmp/rss-dummy-backend
RUN stack install
ENTRYPOINT ["/root/.local/bin/rss-dummy-backend-exe"]
CMD ["--feedsdir", "./rss-sample-files"]
