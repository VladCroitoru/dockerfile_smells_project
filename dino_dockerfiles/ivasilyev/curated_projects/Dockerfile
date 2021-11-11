FROM ivasilyev/jupyter-deploy:latest

RUN mkdir -p /home/docker/scripts && \
    cd /home/docker/scripts/ && \
    git clone https://github.com/ivasilyev/curated_projects.git && \
    git clone https://github.com/ivasilyev/statistical_tools.git

WORKDIR /home/docker/scripts/curated_projects/

ENV PYTHONPATH=/home/docker/scripts/curated_projects/
ENV UTILS_DIR=/home/docker/scripts/curated_projects/meta/scripts/

CMD ["/bin/bash"]

# MANUAL BUILD COMMAND:
# export DOCKER_IMAGE_NAME=curated_projects && docker build -t ${DOCKER_IMAGE_NAME} . && docker tag ${DOCKER_IMAGE_NAME} ivasilyev/${DOCKER_IMAGE_NAME}:latest && docker push ivasilyev/${DOCKER_IMAGE_NAME}:latest
