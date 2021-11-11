FROM hasura/graphql-engine:v2.0.9.cli-migrations-v3
ENV HASURA_GRAPHQL_MIGRATIONS_DIR="/hasura-migrations"
ENV HASURA_GRAPHQL_METADATA_DIR="/hasura-metadata"
COPY ./migrations "${HASURA_GRAPHQL_MIGRATIONS_DIR}"
COPY ./metadata "${HASURA_GRAPHQL_METADATA_DIR}"
WORKDIR /app
COPY ./scripts ./scripts
ENTRYPOINT ["/app/scripts/docker-entrypoint.sh"]
CMD ["graphql-engine", "serve"]
