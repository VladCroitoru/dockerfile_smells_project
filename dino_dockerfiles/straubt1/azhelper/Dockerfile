FROM azuresdk/azure-cli-python:latest
LABEL maintainer="tstraub@cardinalsolutions.com"

# Copy all scripts and have them sourced on bash loading.
COPY scripts/ scripts/
RUN echo -e "\
for f in /scripts/*; \
do chmod a+x \$f; source \$f; \
done;" > ~/.bashrc

RUN ["/bin/bash", "-c", "shopt -s extglob"]
CMD bash
