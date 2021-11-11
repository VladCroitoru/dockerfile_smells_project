# FROM ljnelson/docker-calibre-alpine

# RUN apk update && \
#     apk add --no-cache --upgrade \
    
FROM haskell:8.0

RUN apt-get update -y \
  && apt-get install -y -o Acquire::Retries=10 --no-install-recommends \
  calibre \
  epubcheck
  
# will ease up the update process
# updating this env variable will trigger the automatic build of the Docker image
ENV PANDOC_VERSION "1.19.2.1"

# install pandoc
RUN cabal update && cabal install pandoc-${PANDOC_VERSION}

WORKDIR /source

ENTRYPOINT ["/root/.cabal/bin/pandoc"]

CMD ["--help"]
