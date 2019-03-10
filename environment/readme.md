# Container Summary

## App Container
* Building and running the app.Dockerfile sets up an apache server which hosts the api.
* The devMongoContainerIp from the config is added as an environment variable to connect to the DB.
* The container runs on a created docker network called booknet.
* No assigned IP Address.
* port forwarding 80:80.
* The python modules are pip installed.


## DB Container
* Building and running the db.Dockerfile sets up a mongodb server.
* Running the run_db_container.sh script without arugment uses the devMongoContainerIp as the container's IP.
* If you add the "unit_tests" arg when calling the run_db_container.sh then it'll use the testMongoContainerIp IP.
* The container runs on a created docker network called booknet.


## Unit Test Container
* Building the container will pip install the book_api modules.
* Running the container will run the unit tests from your local environments
* Therefore to run new tests you only need to run the container, but to edit the code that the tests run against, you need to build
* The container runs on a created docker network called booknet.