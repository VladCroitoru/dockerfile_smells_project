FROM python:3.8.5
LABEL version="0.1"
LABEL maintainer="Dror Milo"
LABEL description="A Docker container of a Jupiter Notebook with a LeNet Neural Network \
				   trained and utilied for fruits recognition"

WORKDIR /data

COPY . /data

RUN pip install pandas=1.2.4 /
	pip install jupyter /
	pip install scikit-learn=0.24.1 /
	pip install torch=1.4.0 /
	pip install torchvision=0.2.2 /
	pip install matplotlib=3.3.4
	
EXPOSE 8888

CMD ["jupyter","notebook","--ip=0.0.0.0","--port=8888","--no-browser","--allow-root"]
				   
