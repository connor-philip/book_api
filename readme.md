# book_api
Exactly what it sounds like, a book API. Built for practise.

Python3. Apache. MongoDB.

## Set Up

#### Application
To run the application there's docker files to run the different aspects. There's bash scripts to control these within the environment dir and each container's directory.

If you choose to run Vagrant then these containers will be built and run on provisioning the vagrant VM.

After starting the application, you can connect to the api by going localhost in a browser (or 200.2.2.2 if using Vagrant).

#### Dev environment
There's a optional [Vagrant](https://www.vagrantup.com/downloads.html "https://www.vagrantup.com/downloads.html") environment available for a dev environment so that you won't need to install any other software on your host machine.

If you choose not to use Vagrant all that you really need is a terminal that can run bash scripts ([such as git bash if on windows](https://gitforwindows.org/index.html "https://gitforwindows.org/index.html")) and [Docker](https://www.docker.com/get-started "https://www.docker.com/get-started").

See [environment/readme.md](https://github.com/connor-philip/book_api/blob/master/environment/readme.md) for notes on the different environments used.

