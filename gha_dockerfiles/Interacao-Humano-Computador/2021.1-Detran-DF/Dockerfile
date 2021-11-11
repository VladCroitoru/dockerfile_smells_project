FROM python:3.8-slim
VOLUME /pages
WORKDIR /pages/
RUN pip3 install mkdocs==1.1 mkdocs-material==4.6.3
EXPOSE 8000
ENTRYPOINT ["mkdocs"]