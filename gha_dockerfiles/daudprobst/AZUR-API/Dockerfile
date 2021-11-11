FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./

#ENV FLASK_APP="src/app.py"
#EXPOSE 5000

CMD ["python","src/app.py"] 
#, "--host", "0.0.0.0"]

# docker build -t azur-3000 .
# docker run -p 5000:5000 -ti azur-3000