FROM gcr.io/tensorflow/tensorflow

ADD . /tf

WORKDIR /tf

RUN chmod u+x run_and_board.sh

ENTRYPOINT ["bash", "./run_and_board.sh"]

