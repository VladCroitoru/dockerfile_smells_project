###### Docker image
FROM qnib/alplain-node

ARG SWAGGER_VER=2.10.5
RUN npm install -g http-server \
 && wget -qO /tmp/swagger-editor.zip https://github.com/swagger-api/swagger-editor/releases/download/v${SWAGGER_VER}/swagger-editor.zip \
 && cd /opt/ \
 && unzip /tmp/swagger-editor.zip \
 && rm -f /tmp/swagger-editor.zip
ADD opt/swagger-editor/spec-files/ /opt/swagger-editor/spec-files/
ADD opt/swagger-editor/config/defaults.json /opt/swagger-editor/config/
WORKDIR /opt/
CMD ["http-server", "swagger-editor"]
