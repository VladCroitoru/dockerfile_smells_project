FROM openjdk:7

RUN apt-get update && apt-get install -y curl
RUN curl -s "https://get.sdkman.io" | bash
RUN /bin/bash -c "source \"/root/.sdkman/bin/sdkman-init.sh\" && sdk install grails 2.3.5"
CMD ["grails", "clean", "war"]
