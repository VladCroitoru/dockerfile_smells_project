FROM python:3.5.1
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/catherinejelder/packing_list.git /usr/src/app/
RUN python /usr/src/app/unit_tests.py
EXPOSE 8080
CMD ["python", "-u", "/usr/src/app/server.py"]
