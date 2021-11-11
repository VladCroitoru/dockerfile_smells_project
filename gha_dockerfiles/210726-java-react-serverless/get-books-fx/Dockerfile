FROM amazon/aws-lambda-java:8.al2

WORKDIR /home/app
COPY target/classes ${LAMBDA_TASK_ROOT}
COPY target/dependency/* ${LAMBDA_TASK_ROOT}/lib/

CMD ["com.revature.get_books.GetBooksHandler::handleRequest"]