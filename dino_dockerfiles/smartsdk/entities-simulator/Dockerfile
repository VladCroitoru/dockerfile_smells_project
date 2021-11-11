FROM python:3.6

RUN pip install requests

RUN mkdir /src
WORKDIR /src

COPY README.md /src/
COPY *.py /src/

ENTRYPOINT ["python"]
CMD ["entities_simulator.py"]
