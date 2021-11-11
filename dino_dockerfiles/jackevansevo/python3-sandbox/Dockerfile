FROM python:alpine
RUN apk add --no-cache vim curl git musl-dev gcc && \
        pip install --upgrade pip && \
        pip install ipython takoshell && \
        curl https://raw.githubusercontent.com/Jackevansevo/Dotfiles/master/ipython_config.py --create-dirs -o ~/.ipython/profile_default/ipython_config.py
CMD "python"
