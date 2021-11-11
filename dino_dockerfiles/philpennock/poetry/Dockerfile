# This is a Dockerfile with no executable
# It's a bit silly, as really you should use tarballs normally,
# especially for something this small.
#
# But for much larger data-sets, being able to use Docker Image
# caching pays off, as you just pull when there's a difference.
#
# In an ideal world, you could directly specify that a Docker
# VOLUME come from a Docker image, or have another mechanism for
# sharing Containers if not that.
#
FROM scratch
COPY poems/* /
ENTRYPOINT ["/nonexistent"]

LABEL maintainer="Phil Pennock"
LABEL comment="public-domain poetry sample data set"
