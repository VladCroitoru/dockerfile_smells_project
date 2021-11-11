FROM python:3.8.2-alpine

WORKDIR /USFA_WEBSITE

ADD . /USFA_WEBSITE

RUN pip install -r requirements.txt

CMD ["python","application.py"]


#docker login -u "thomaspark1" -p "Asiandegamers1" docker.io
#docker push {{username}}/{{imagename}}:{{version}}

#you have to tag your image before pushing them


#docker image build -t usfa_website .

#docker ps -a

# docker run --rm -p 5000:5000 usfa_website
#running locally on http://localhost:5000/
#docker stop [ID]


#docker run -d -p 80:80 --name ddocker imageocker-tutorial docker101tutorial



