#####
## Dockerfile for building a 'data container' that contains the description files
##
## This data container is used to populate a volume in the Indexer deployment.
#####

ARG BASE_IMAGES_REGISTRY=registry.ceda.ac.uk/base-images
ARG BASE_IMAGES_VERSION

FROM ${BASE_IMAGES_REGISTRY}/centos7:${BASE_IMAGES_VERSION}

# Create a user to run the container instead of root
ENV INDEXER_UID 1001
ENV INDEXER_GID 1001
ENV INDEXER_USER indexer
ENV INDEXER_GROUP indexer
RUN groupadd --gid $INDEXER_GID $INDEXER_GROUP && \
    useradd \
      --no-create-home \
      --no-user-group \
      --gid $INDEXER_GID \
      --shell /sbin/nologin \
      --uid $INDEXER_UID \
      $INDEXER_USER

# Make a directory for the json tags and populate it
COPY ./descriptions/ /app/descriptions/

USER $INDEXER_UID
