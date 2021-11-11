FROM projectatomic/atomicapp:latest

MAINTAINER The ViaQ Community <community@TBA>

LABEL io.projectatomic.nulecule.providers="docker" \
      io.projectatomic.nulecule.specversion="0.0.2" \
      RUN="docker run --rm \${OPT1} --privileged -v `pwd`:/atomicapp -v /run:/run -v /:/host --net=host --name \${NAME} -e NAME=\${NAME} -e IMAGE=\${IMAGE} \${IMAGE} -v \${OPT2} run \${OPT3} \${IMAGE}"

ADD /Nulecule /Dockerfile /application-entity/
# we don't have anything for the artifacts directory (yet)
# nulecule requires an artifacts directory
# we can't have an empty directory in the git repo
# having an artifacts directory with a README fails
# so the solution is to have the Dockerfile create the directory
#ADD /artifacts /application-entity/artifacts
RUN mkdir -p /application-entity/artifacts
