FROM garland/aws-cli-docker
RUN pip install awscli --upgrade
ADD https://get.docker.com/builds/Linux/x86_64/docker-latest /usr/bin/docker
RUN chmod +x /usr/bin/docker
ENTRYPOINT aws ecr get-login | /bin/bash && docker tag $IMAGE $TARGET && docker push $TARGET
