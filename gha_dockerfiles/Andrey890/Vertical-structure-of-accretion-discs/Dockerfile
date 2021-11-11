FROM mesa2py

COPY /requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY bin /app
WORKDIR /app

RUN mkdir -pv /app/fig
VOLUME /app/fig

CMD ["python", "vs.py"]
