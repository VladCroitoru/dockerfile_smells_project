FROM python:2.7

LABEL description="Filter Proxy"
LABEL version="0.1"

ENV NUMPY 1.12.1
ENV SCIPY 0.19.0
ENV SCIKIT 0.18.1
ENV UWSGI 2.0.15
ENV FILTERPROXY_SETTINGS /app/settings.py

# Install uWSGI
RUN pip install uwsgi==${UWSGI}
COPY uwsgi.ini /etc/uwsgi/

# Install filterproxy
COPY app /app
COPY data/svm_linear_classifier.pkl /app/svm_linear_classifier.pkl
COPY data/vectorizer.pkl /app/vectorizer.pkl
COPY filterproxy /app/filterproxy
COPY setup.py /app/setup.py
COPY settings.py /app/settings.py
COPY tests /app/tests
RUN pip install numpy==${NUMPY} SciPy==${SCIPY} scikit-learn==${SCIKIT} && \
    cd /app && \
    python setup.py install
RUN cd /app/tests && python test_app.py

WORKDIR /app

EXPOSE 8080

CMD ["/usr/local/bin/uwsgi", "--ini", "/app/uwsgi.ini"]
