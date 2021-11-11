FROM maven:3.3-jdk-7

ENV SWAGGER_CODEGEN_DIR		/opt/swagger-codegen
ENV SWAGGER_CODEGEN_CLI		$SWAGGER_CODEGEN_DIR/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar

RUN git clone -b master https://github.com/swagger-api/swagger-codegen $SWAGGER_CODEGEN_DIR 
RUN git clone -b master https://github.com/sapienstech/typescript-angular2-swagger-codegen.git $SWAGGER_CODEGEN_DIR/output/typescript-angular2-swagger-codegen

RUN cd $SWAGGER_CODEGEN_DIR \
 && mvn package

RUN cd $SWAGGER_CODEGEN_DIR/output/typescript-angular2-swagger-codegen \
 && mvn package

WORKDIR /opt/swagger-codegen

ENTRYPOINT ["java", "-cp", "modules/swagger-codegen-cli/target/swagger-codegen-cli.jar:output/typescript-angular2-swagger-codegen/target/typescript-angular2-swagger-codegen-1.1.jar", "io.swagger.codegen.SwaggerCodegen"]

CMD ["help"]