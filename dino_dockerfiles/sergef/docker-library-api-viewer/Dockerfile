FROM sergef/docker-library-nginx:1.12.0

ENV SWAGGER_UI_VERSION 3.0.17
WORKDIR /app

# https://github.com/swagger-api/swagger-ui/archive/v3.0.17.tar.gz
ADD swagger-ui-${SWAGGER_UI_VERSION}.tar.gz /opt
COPY sample.json /app

RUN cp /opt/swagger-ui-${SWAGGER_UI_VERSION}/dist/* /app \
  && sed -i 's/http:\/\/petstore.swagger\.io\/v2\/swagger\.json/sample\.json/g' /app/index.html \
  && sed -i 's/\.\///g' /app/index.html
