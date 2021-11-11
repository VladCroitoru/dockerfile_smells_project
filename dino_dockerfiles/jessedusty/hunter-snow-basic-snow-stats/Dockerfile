FROM python:3-alpine
WORKDIR /root
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY server.py ./
COPY website_parser.py ./
CMD [ "python", "server.py" ]
EXPOSE 80
