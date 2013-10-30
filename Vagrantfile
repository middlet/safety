#
# city safety
#

# config options
ip = '192.168.0.53'
hostname = 'safetytron'
ram = '512'

# provision script
$script = <<SCRIPT
sudo apt-get update
sudo apt-get install -y git
sudo apt-get install -y python-pip
# for functional testing
sudo apt-get install -y firefox
sudo apt-get install -y xvfb
# python packages
sudo pip install -r /vagrant/requirements.txt
SCRIPT

Vagrant.configure("2") do |config|
    config.vm.box = 'precise32'
    config.vm.box_url = 'http://files.vagrantup.com/precise32.box'
    config.vm.hostname = hostname
    config.vm.network :private_network, ip: ip
    config.vm.network :forwarded_port, guest: 31337, host: 31337

    config.vm.provider :virtualbox do |vb|
        vb.customize [
            'modifyvm', :id,
            '--name', hostname,
            '--memory', ram
        ]
    end
    config.vm.provision :shell, :inline => $script
end
