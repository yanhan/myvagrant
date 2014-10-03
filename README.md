# My Vagrant Setup

My own Vagrant setup, mostly used on a Mac OS X machine for a headless Linux
system. Vagrant 1.6.3 is used for this Vagrant setup.
Provisioning is done using [Ansible](http://www.ansible.com/home).

The Vagrant's name is `myvagrant`.

**NOTE:** This is still very much a WIP.

## Software Requirements

- [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](http://www.vagrantup.com/) 1.6.3
- Python 2.7.x
- virtualenv
- [Ansible](http://www.ansible.com/home) 1.6.6

We assume you know how to install Virtualbox, Vagrant and Python.
We'll cover the installation of virtualenv and Ansible below.

## Software Requirements Setup

### Installing virtualenv

    sudo apt-get install python-virtualenv
    virtualenv venv                           # create venv folder

### Installing Ansible

    . venv/bin/activate                # enter virtualenv
    pip install -r requirements.txt

## SSH Config

The following entry should be in your SSH config (most likely at
`$HOME/.ssh/config`) for the Vagrant provisioning to run smoothly:

    Host myvagrant
        Hostname 127.0.0.1
        Port 2222
        User vagrant

## Vagrant Password file

There should be a `ansible/roles/vagrant/files/vagrant_password.txt` file
containing a single line which is the password of the `vagrant` user.

## Vagrant Up

Now we are ready to initialize and provision the Vagrant.

    . venv/bin/activate    # enter virtualenv so we can use Ansible
    vagrant up             # starts and provisions the vagrant

Everything's ready from here on.
