FROM java:8

COPY JavaAutoBuild.java .
COPY index.html .
COPY style.css .
COPY vue.js .
COPY images .

RUN javac JavaAutoBuild.java

CMD ["java", "JavaAutoBuild"]
