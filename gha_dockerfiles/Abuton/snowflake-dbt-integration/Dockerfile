# syntax=docker/dockerfile:1
FROM python:3.9.7-slim
# Update and install system packages
RUN apt-get update \
    && apt-get -y install libpq-dev gcc 

RUN pip install psycopg2-binary==2.8.4 && \
    pip install dbt-mysql
# EXPOSE 8001
# COPY . .
# CMD ["dbt", "docs", "serve"]

# Set environment variables
ENV DBT_DIR=/dbt

# Set working directory
WORKDIR $DBT_DIR

COPY . .

ENTRYPOINT [ "dbt" ]

# https://towardsdatascience.com/oh-my-dbt-data-build-tool-ba43e67d2531