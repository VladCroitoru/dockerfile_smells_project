FROM ubuntu:precise
MAINTAINER ODL DevOps <mitx-devops@mit.edu>
COPY build /build
RUN bash -ex /build/docker_build

# Add copies to Dockerfile incase they don't want local mode
COPY test_course /test_course
