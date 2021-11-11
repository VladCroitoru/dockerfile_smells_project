from python:3-alpine
workdir /home
RUN apk --no-cache add curl ripgrep npm
copy requirements.txt package.json package-lock.json ./

# install web assets and move them to static folder
run npm install && mkdir -p src/static/media/fonts src/static/media/css src/static/media/js && cp node_modules/bootstrap/dist/fonts/* src/static/media/fonts/ && cp node_modules/bootstrap/dist/css/bootstrap.min.css src/static/media/css/ && cp node_modules/bootstrap/dist/js/bootstrap.min.js node_modules/jquery/dist/jquery.min.js src/static/media/js/ && rm -rf node_modules

run pip install -r requirements.txt
copy . .
expose 5000
cmd ["python", "src/server.py", "wiki"]
