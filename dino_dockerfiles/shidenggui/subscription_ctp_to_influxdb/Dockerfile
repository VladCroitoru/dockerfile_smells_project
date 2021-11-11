FROM python:3.5


RUN git clone https://github.com/lovelylain/pyctp
RUN cd pyctp && \
    python setup.py build && \
    python setup.py install


RUN git clone https://github.com/shidenggui/easyctp
RUN cd easyctp && \
    pip install -r requirements.txt && \
    python setup.py install

WORKDIR /easyctp
ENTRYPOINT ["python", "scripts/subscription_ctp_to_influxdb.py"]





