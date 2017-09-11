# Tensorflow Playground

This repo can build a docker container which executes the Tensorflow app in `app.py`
and then launches Tensorboard for analysis.

## Running in Docker

```sh
docker build -t tensorflow-app .
docker run -ti -p 6006:6006 tensorflow-app
```

At this point, you should be able to view Tensorboard in your browser at [http://localhost:6006]

