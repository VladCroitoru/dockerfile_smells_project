FROM openjdk:jre-alpine
LABEL author="ZhiFeng Hu <hufeng1987@gmail.com>"


RUN apk update; \
    apk add python2-dev py-pip graphviz ttf-droid ttf-droid-nonlatin curl; \
    pip install mkdocs pygments pymdown-extensions  mkdocs-material ; \
    curl -L https://sourceforge.net/projects/plantuml/files/plantuml.jar/download -o /usr/bin/plantuml.jar ;\
    apk del curl 
COPY plantuml.py /usr/lib/python2.7/site-packages/markdown/extensions/
COPY plantuml /usr/bin/plantuml 
RUN chmod +x /usr/bin/plantuml 

