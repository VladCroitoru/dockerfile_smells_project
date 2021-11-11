# require chrome for tests
FROM gpmikep/docker-node-chrome

# use cache containers
# on gitlab-ci auto mapped to a caching container
# if running locally we need to manually create & attach a caching container
VOLUME ["/src/node_modules", "/src/jspm_packages", "/src/typings"]

WORKDIR /src
