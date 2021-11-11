FROM python:3.9-slim

LABEL org.label-schema.name="astrochun/github-stats-pages"
LABEL org.label-schema.description="Docker image to build static GitHub stats pages"
LABEL org.label-schema.url="https://github.com/astrochun/github-stats-pages"
LABEL maintainer="astro.chun@gmail.com"

COPY github_stats_pages ./github_stats_pages
COPY scripts ./scripts
COPY requirements.txt setup.py ./
COPY README.md .
COPY entrypoint.sh /entrypoint.sh

RUN python setup.py develop

ENTRYPOINT ["/entrypoint.sh"]
