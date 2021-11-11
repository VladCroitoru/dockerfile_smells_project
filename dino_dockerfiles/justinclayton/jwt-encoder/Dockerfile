FROM python
RUN pip install PyJWT
RUN pip install cryptography
COPY jwt-encoder.py /jwt-encoder.py
ENTRYPOINT ["python", "/jwt-encoder.py"]
