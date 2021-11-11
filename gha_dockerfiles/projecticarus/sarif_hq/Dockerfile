# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster
WORKDIR /var/lib/pythonApps
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
# CMD [ "python3", "-m" , "flask", "init-db"]
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
ADD docker_cmd.sh /
RUN chmod +x /docker_cmd.sh
CMD ["/docker_cmd.sh"]