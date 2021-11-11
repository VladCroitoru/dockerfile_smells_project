FROM python:3

RUN pip3 install nameko pymongo pytest ; \
	cd /tmp ; \
	git clone https://github.com/saiqi/nameko-mongodb.git ; \
	cd ./nameko-mongodb ; \
	python3 setup.py install

ENTRYPOINT ["nameko","run","--config","cluster.yml"]
