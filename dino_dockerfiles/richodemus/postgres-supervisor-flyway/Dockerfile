FROM postgres:9.5

RUN apt-get update && apt-get install -y curl supervisor && apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN mkdir /flyway
RUN curl https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/4.0/flyway-commandline-4.0-linux-x64.tar.gz | tar -zxf - --strip 1 -C /flyway/
