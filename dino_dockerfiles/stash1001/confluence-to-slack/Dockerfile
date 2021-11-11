FROM python:2-alpine
RUN pip install beautifulsoup4
RUN pip install Confluence-py
RUN pip install requests
COPY confluence-to-slack-docker.py confluence-to-slack-docker.py
CMD [ "python", "./confluence-to-slack-docker.py" ]