FROM python:3.9

RUN mkdir -p /opt/application/ubademy-back-py
COPY requirements.txt /opt/application/ubademy-back-py
WORKDIR /opt/application/ubademy-back-py

RUN apt-get update
RUN pip install -r requirements.txt
ENV DATABASE_HOST postgres-db
EXPOSE 8080

ENTRYPOINT ["flask", "run", "-h", "0.0.0.0", "-p"]
CMD ["8080"]
