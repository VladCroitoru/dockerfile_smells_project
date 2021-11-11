FROM python:3.6

WORKDIR /app
COPY . /app
EXPOSE 9092
RUN pip3 install pipenv && pipenv install --deploy --system
RUN groupadd -g 984 respondenthome && \
    useradd -r -u 984 -g respondenthome respondenthome
USER respondenthome
ENTRYPOINT ["python3"]
CMD ["run.py"]
