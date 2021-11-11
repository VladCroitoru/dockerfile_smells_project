FROM java:openjdk-7u101-jdk

ENV app_dir /usr/src/changedistiller

COPY . ${app_dir}
WORKDIR ${app_dir}

RUN apt-get update && apt-get install -y maven
RUN ${app_dir}/build.sh
RUN mvn install

VOLUME ${app_dir}/target

ENTRYPOINT ["mvn", "test"]
