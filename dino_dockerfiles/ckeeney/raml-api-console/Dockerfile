FROM scardon/ruby-node-alpine
RUN apk update \
    && apk add ca-certificates wget git \
    && update-ca-certificates
RUN gem install sass
RUN npm install -g grunt-cli bower karma grunt-karma --save-dev
RUN git clone https://github.com/mulesoft/api-console.git /api-console

WORKDIR /api-console

RUN git checkout ${API_CONSOLE_VERSION:-v3.0.7} \
    && mkdir -p /api-console/dist/apis \
    && mv /api-console/dist/examples/simple.raml /api-console/dist/apis/main.raml

RUN npm install
RUN bower --allow-root install

RUN sed -i 's/<raml-initializer><\/raml-initializer>/<raml-console-loader src="apis\/main.raml"><\/raml-console-loader>/g' /api-console/dist/index.html

# Convenient mount point
RUN ln -sf /api-console/dist/apis /apis

# for live reload
EXPOSE 35729

# for http
EXPOSE 9000
CMD ["grunt", "connect:livereload", "watch"]
