Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"
  config.vm.network :private_network, ip: "200.2.2.2"
  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.vm.synced_folder ".", "/vagrant/book_api"
  config.vm.provision :shell, name: "apt_install_python3.sh",
        path: "setup/setup_scripts/apt_install_python3.sh",
        upload_path: "/vagrant/book_api/setup/setup_scripts/apt_install_python3.sh"
  config.vm.provision :shell, name: "apt_install_docker.sh",
        path: "setup/setup_scripts/apt_install_docker.sh",
        upload_path: "/vagrant/book_api/setup/setup_scripts/apt_install_docker.sh"

  config.vm.provision :shell, name: "create_docker_network.sh",
        path: "setup/container_scripts/create_docker_network.sh",
        upload_path: "/vagrant/book_api/setup/container_scripts/create_docker_network.sh"
  config.vm.provision :shell, name: "build_app_container.sh",
        path: "setup/container_scripts/build_app_container.sh",
        upload_path: "/vagrant/book_api/setup/container_scripts/build_app_container.sh"
  config.vm.provision :shell, name: "build_db_container.sh",
        path: "setup/container_scripts/build_db_container.sh",
        upload_path: "/vagrant/book_api/setup/container_scripts/build_db_container.sh"
end