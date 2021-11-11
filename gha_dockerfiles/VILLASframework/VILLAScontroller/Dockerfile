FROM python:3.9

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

COPY . /tmp/controller
RUN cd /tmp/controller && \
	python3 setup.py sdist && \
	pip3 install dist/*.tar.gz && \
	rm -rf /tmp/controller

ENTRYPOINT [ "villas-controller" ]
