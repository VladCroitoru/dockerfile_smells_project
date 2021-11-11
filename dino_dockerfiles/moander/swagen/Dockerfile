FROM moander/java8

MAINTAINER Morten Andersen <moander@outlook.com>

ENV SWAGGER_CODEGEN_CLI_VERSION=2.2.1

RUN wget http://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/${SWAGGER_CODEGEN_CLI_VERSION}/swagger-codegen-cli-${SWAGGER_CODEGEN_CLI_VERSION}.jar -O swagger-codegen-cli.jar \
 && printf '#!/bin/bash\nexec java -jar /swagger-codegen-cli.jar "$@" 1>&2\n' > /bin/swagger-codegen \
 && chmod a+x /bin/swagger-codegen \
 && ln /bin/swagger-codegen /bin/swagen

VOLUME /swag

WORKDIR /swag

ENTRYPOINT [ "/bin/swagen" ]

CMD [ "help" ]


