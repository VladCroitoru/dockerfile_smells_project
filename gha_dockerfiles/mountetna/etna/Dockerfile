FROM etna-base-dev
ENV ETNA_GEM_DEVELOPMENT=1
COPY . /etna
RUN rm -rf /app && ln -sfT /etna /app
