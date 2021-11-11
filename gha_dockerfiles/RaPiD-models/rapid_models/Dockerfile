FROM python:3.8-bullseye

RUN apt-get update 

# Install python packages for sphinx build
RUN python -m pip install --upgrade pip

COPY ./requirements_dev.txt .
# RUN pip install -r requirements.txt
RUN pip install -r requirements_dev.txt

COPY . .

# Build docs to docs/_build
RUN cd docs
RUN sphinx-apidoc -o . ../src/rapid_models
RUN sphinx-build -M html ./docs ./docs/build
# RUN make html

# Build package
RUN cd ..
RUN python ./setup.py sdist
RUN mkdir ./docs/build/html/dist
RUN mv ./dist/*.tar.gz ./docs/build/html/dist/

# Create new image
FROM nginx:alpine

WORKDIR /app
# Copy the static build assets to /app dir
COPY --from=0 ./docs/build/html/ .
# Copy in the nginx config file
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
# All files are in, start the web server
CMD ["nginx"]