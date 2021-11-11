FROM python:3.8.11
RUN pip install --upgrade pip
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY . /app
WORKDIR /app
RUN pytest
EXPOSE 5000
RUN ls -lah .
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT [ "./docker-entrypoint.sh" ]