FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY data.csv ./
COPY fruit_basket.py ./

ENTRYPOINT [ "python", "./fruit_basket.py" ]
CMD [ "data.csv"]