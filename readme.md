# book_api
Exactly what it sounds like, a book API built for practise.

## Set Up
For a dev environment you can run it locally or use the Vagrantfile provided.
See /setup/readme.md for notes on the different environments used.

#### Vagrant
Make sure you have [Vagrant](https://www.vagrantup.com/downloads.html "Download Vagrant here; https://www.vagrantup.com/downloads.html") installed.
Once it's installed, cd to the book_api dir in a terminal and enter: `vagrant up`. This will create a dev environment for you. If you're interested in the steps, take a look at the Vagrantfile.

To connect to the environment in a terminal use `vagrant ssh`

You can also connect to the server through by visiting the IP of the vm in a browser, set to 200.2.2.2 by default in the Vagrantfile

To tear down the environment, use `vagrant destroy`

#### Locally
I haven't added a script run set up a dev environment locally. However all the script you need are in the setup directory. These scripts are designed to run in a Linux(Ubuntu) environment so if you're using another OS you'll need to take the appropriate actions for your OS.

Take a look in the Vagrantfile to see the steps it takes, and run the scripts (in order\*)
\* Not all the scripts need to be run in order, but it's required to run most of the docker related scripts in the order within the Vagrantfile
