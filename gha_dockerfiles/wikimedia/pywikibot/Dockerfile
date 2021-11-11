FROM python:3.8-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip3 install .

ENV PYTHONPATH=/code:/code/scripts

ENTRYPOINT ["python", "/code/pwb.py"]
CMD ["version"]
