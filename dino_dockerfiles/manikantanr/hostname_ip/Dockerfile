FROM alpine:3.6
RUN apk --update add python py-pip && pip install flask
COPY . .
EXPOSE 8000
CMD python app.py
