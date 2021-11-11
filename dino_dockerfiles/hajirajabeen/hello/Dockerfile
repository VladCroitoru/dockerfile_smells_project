FROM java:7
COPY hello.java .
RUN java -Xmx2048m -Xms2048m
RUN javac hello.java
CMD ["java","hello"]
