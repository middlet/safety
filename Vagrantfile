#
# website autobuild vm
#

# config options
ip = '10.53.0.2'
hostname = 'safety'
ram = '512'

$script = <<SCRIPT
sudo apt-get update
sudo apt-get install -y python-pip python-dev

# postgis
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get install -y postgresql-9.3-postgis-2.1 libpq-dev
# create user
sudo -u postgres createuser -s vagrant # superuser
# create db
sudo -u postgres createdb safety
sudo -u postgres psql -d safety -c "CREATE EXTENSION postgis;"
sudo -u postgres psql -d safety -c "CREATE EXTENSION postgis_topology;"

sudo pip install -r /vagrant/requirements.txt
# gis utils
sudo apt-get install -y gdal-bin

# update the bash prompt
sed -i -e "s/;32m/;35m/" .bashrc
sed -i -e "s/\#force/force/" .bashrc
SCRIPT

Vagrant.configure("2") do |config|
    config.vm.box = 'tahr32'
    config.vm.box_url = 'https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-i386-vagrant-disk1.box'
    config.vm.hostname = hostname
    config.vm.network :private_network, ip: ip
    config.vm.network "forwarded_port", guest: 8000, host: 8000

    config.vm.provider :virtualbox do |vb|
        vb.customize [
            'modifyvm', :id,
            '--name', hostname,
            '--memory', ram
        ]
    end

    config.vm.provision :shell, :inline => $script
end
