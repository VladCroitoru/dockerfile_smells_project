FROM clojure

MAINTAINER Simone Mosciatti <simone@mweb.biz>

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY project.clj /usr/src/app/

RUN lein deps

COPY . /usr/src/app

RUN mv "$(lein uberjar | sed -n 's/^Created \(.*standalone\.jar\)/\1/p')" app-standalone.jar

EXPOSE 8000

ENTRYPOINT ["java", "-jar", "app-standalone.jar"]
