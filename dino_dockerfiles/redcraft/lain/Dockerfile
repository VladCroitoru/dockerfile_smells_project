FROM ubuntu

RUN apt-get update && apt-get install -y \
	nodejs \
	npm \
	curl \
&& rm -rf /var/lib/apt/lists/*

COPY ./ /opt/app/

WORKDIR /opt/app/

RUN useradd -d /opt/app node
RUN npm install

ARG IMG_VERSION
ENV IMG_VERSION ${IMG_VERSION:-v1.0.0}

LABEL author="Maxim Gurkin" \
      location="Singapore" \
      build_version=$IMG_VERSION

EXPOSE 3000
VOLUME /opt/app/img

USER node
STOPSIGNAL SIGKILL
HEALTHCHECK --interval=10s --timeout=3s CMD if [ $(curl http://localhost:3000/healthcheck) = "unhealthy" ]; then exit 1; else exit 0; fi
ONBUILD RUN echo onbuild
#CMD ["nodejs", "app.js"]
ENTRYPOINT ["nodejs"]
CMD ["app.js"]
