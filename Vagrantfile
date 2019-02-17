Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"
  config.vm.network :private_network, ip: "200.2.2.2"
  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.vm.synced_folder ".", "/vagrant/book_api"

  # Install scripts
  config.vm.provision :shell, name: "apt_install_python3.sh",
        path: "setup/setup_scripts/apt_install_python3.sh",
        upload_path: "/vagrant/book_api/setup/setup_scripts/apt_install_python3.sh"

  config.vm.provision :shell, name: "apt_install_docker.sh",
        path: "setup/setup_scripts/apt_install_docker.sh",
        upload_path: "/vagrant/book_api/setup/setup_scripts/apt_install_docker.sh"

  config.vm.provision :shell, name: "pip_install_packages.sh",
        path: "setup/setup_scripts/pip_install_packages.sh",
        upload_path: "/vagrant/book_api/setup/setup_scripts/pip_install_packages.sh"

  # Env setup
  config.vm.provision :shell, name: "create_dev_env_variable.sh",
        path: "setup/setup_scripts/create_dev_env_variable.sh",
        upload_path: "/vagrant/book_api/setup/setup_scripts/create_dev_env_variable.sh"

  # Docker container setup
  config.vm.provision :shell, name: "create_docker_network.sh",
        path: "setup/setup_scripts/create_docker_network.sh",
        upload_path: "/vagrant/book_api/setup/setup_scripts/create_docker_network.sh"

  config.vm.provision :shell, name: "build_app_container.sh",
        path: "setup/app_container/build_app_container.sh",
        upload_path: "/vagrant/book_api/setup/app_container/build_app_container.sh"
  config.vm.provision :shell, name: "run_app_container.sh",
        path: "setup/app_container/run_app_container.sh",
        upload_path: "/vagrant/book_api/setup/app_container/run_app_container.sh"

  config.vm.provision :shell, name: "build_db_container.sh",
        path: "setup/db_container/build_db_container.sh",
        upload_path: "/vagrant/book_api/setup/db_container/build_db_container.sh"
  config.vm.provision :shell, name: "run_db_container.sh",
        path: "setup/db_container/run_db_container.sh",
        upload_path: "/vagrant/book_api/setup/db_container/run_db_container.sh"

  # Run Unit Tests
  config.vm.provision :shell, name: "run_db_container.sh",
        path: "setup/db_container/run_db_container.sh",
        upload_path: "/vagrant/book_api/setup/db_container/run_db_container.sh",
        args: " unit_test"
  config.vm.provision :shell, name: "build_unit_test_container.sh",
        path: "setup/unit_test_container/build_unit_test_container.sh",
        upload_path: "/vagrant/book_api/setup/unit_test_container/build_unit_test_container.sh"
  config.vm.provision :shell, name: "run_unit_test_container.sh",
        path: "setup/unit_test_container/run_unit_test_container.sh",
        upload_path: "/vagrant/book_api/setup/unit_test_container/run_unit_test_container.sh"
end