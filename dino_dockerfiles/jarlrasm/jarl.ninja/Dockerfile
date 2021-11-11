FROM nginx
RUN apt-get update   && apt-get install --no-install-recommends --no-install-suggests -y  curl default-jre  && rm -rf /var/lib/apt/lists/*
RUN curl https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein > /usr/bin/lein && chmod 755 /usr/bin/lein
ENV LEIN_ROOT=1
RUN lein
COPY . /app
RUN cd app && lein cljsbuild once release && cp -r resources/public/. /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
