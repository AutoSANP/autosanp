# AutoSANP

Policy-Driven Automated System Administration and Network Management Platform

## Project Description

Modern IT environments, such as university computer labs, require administrators to manage multiple computers, servers, and network services simultaneously. Performing administrative tasks manually on each system can be time‑consuming, repetitive, and prone to configuration errors. Tasks such as installing software packages, configuring services, managing users, and enforcing policies for security, database, network, and server configurations must be applied consistently across all machines.

AutoSANP (Automated System Administration and Network Policy platform) is a centralized automation framework developed to manage a real computer lab infrastructure efficiently. While the system is being tested in a virtual environment using VirtualBox VMs, it is designed to be deployed directly on actual lab machines. The platform allows a single controller machine to manage multiple client systems remotely through secure connections, ensuring consistency and compliance with predefined policies.

By using AutoSANP, administrators can automate repetitive configuration tasks, enforce security, database, network, and server policies, and maintain uniform system settings across all computers, whether virtual or physical.

## Objectives

* Demonstrate centralized system administration using automation tools.
* Reduce manual system configuration tasks.
* Ensure consistent configuration across multiple machines.
* Implement policy‑based system management.
* Provide a virtual environment for testing before real lab deployment.

## Target Users

* System administrators
* DevOps engineers
* IT students learning infrastructure automation
* Educational institutions managing computer labs

## System Architecture / Design

The system follows a Controller–Client architecture.

### Components

**Controller Node**

* Central machine responsible for automation.
* Runs Ansible and executes playbooks.
* Stores inventory and policy definitions.

**Client Nodes**

* Managed machines in the network (can be VMs or physical lab computers).
* Receive configuration commands from the controller.
* Execute tasks to apply changes according to security, database, network, and server policies.

**Automation Engine**

* Implemented using Ansible.
* Executes playbooks and roles to enforce policies.

**Secure Communication Layer**

* SSH used for remote communication.
* SSH key authentication used for password‑less automation.

### Workflow

1. Administrator defines policies using Ansible playbooks.
2. Controller reads the inventory of client machines.
3. Controller connects to clients via SSH.
4. Playbooks execute tasks on remote machines.
5. Client machines apply configurations automatically.

## Technologies Used

**Programming / Scripting**: Python, YAML, Bash
**Automation Tools**: Ansible
**Virtualization (for testing)**: VirtualBox
**Operating System**: Lubuntu / Ubuntu Linux
**Network Tools**: SSH (Secure Shell)
**Version Control**: Git, GitHub 

## Installation Instructions (Prototype using VMs)

### Requirements

* VirtualBox installed (for testing)
* PC's which are connected each other and one must taken as the Controller and other PC's act as clients.
* Linux ISO (Lubuntu/Ubuntu)
* Internet connection

### Steps

1. **Define Controller and Client Design**

   * Controller PC
   * Define Client PC's
   * Ensure all machines are connected to the same internal network.
   * Controller generated key pairs
   * Copy public key to client PC's

2. **Install Required Packages (on each client)**

```
sudo apt update
sudo apt install openssh-server -y
sudo systemctl enable ssh
sudo systemctl start ssh

```

3. **Setup SSH Authentication (on controller)**

```
sudo apt update
sudo apt install openssh-server -y
sudo systemctl enable ssh
sudo systemctl start ssh
ssh-keygen
ssh-copy-id user@client-ip

```

4. **Install Ansible (Controller Only)**

```
sudo apt update
sudo apt install ansible -y
```

5. **Create Project Workspace**

```
mkdir ~/autosanp
cd ~/autosanp
```

> **Note:** In a real lab deployment, replace VM IPs with actual machine IPs and follow the same configuration steps for each physical client computer.

## Usage Instructions

1. **Create Inventory File containing IP Addresses**
   Example `hosts.ini`:

```
[clients]
192.168.10.20
192.168.10.21
192.168.10.22
```

2. **Test Connectivity**

```
ansible -i inventory.ini all -m ping
```

Expected Output: `client1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}`

3. **Run Automation Playbook**

```
ansible-playbook -i inventory.ini install_apache.yml
```

This installs Apache web server on all client machines - Initial Manual Check.

## Dataset

This project does not use an external dataset. It operates on virtual or physical machines within a managed network environment.

## Project Structure

```
autosanp/
│
├── app/
│   ├── app.py
│   ├── dashboard.py  
├── data/
│   ├── autosanp_logs.json
│   ├── hosts.ini
|   ├── policy_states.json
|
├── logs/
|  
├── policies/
│   ├── database_policy.yml
│   ├── security_policy.yml
│   ├── server_policy.yml
├── secrets/
└── README.md
```

## Screenshots / Demo

Suggested screenshots to include:

* VirtualBox virtual network setup (prototype)
* SSH connection from controller to client
* Ansible ping test
* Playbook execution results
* Apache web server running on client
* Short demo video showing automation process

## Contributors

| Name                    | Role                                             |
| ----------------------- | ------------------------------------------------ |
| P.N Maleesha Dilshan    | Virtual environment setup and Ansible automation |
| H.PTharindu Sampath     | Network configuration and system connectivity    |
| H.A.S.R.H. Arachchi     | Automation playbook development                  |
| H.D.T.R. Abhayawardhana | Automation policy implementation and testing     |
| D.M.H.I. Balasooriya    | System architecture and repository management    |

## Contact Information

Institution: Department of Computer Science,University of Jaffna.
For questions or collaboration, contact any team member via the emails listed in the project documentation.



## License

The Project has Licensed Under MIT License
