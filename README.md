# AutoSANP

## Policy-Driven Automated System Administration and Network Management Platform

---

## Project Description

Modern IT environments often require administrators to manage multiple computers, servers, and network services simultaneously. Performing administrative tasks manually on each system can be time‑consuming, repetitive, and prone to configuration errors. Tasks such as installing software packages, configuring services, managing users, and enforcing security policies must be applied consistently across all machines in a network.

AutoSANP (Automated System Administration and Network Policy platform) is a prototype automation framework designed to simplify system administration by using centralized management and policy‑driven automation. The system allows a single controller machine to manage multiple client systems remotely through secure connections.

The platform demonstrates how automation tools can be used to perform administrative tasks across multiple machines efficiently. By using predefined policies and automation scripts, administrators can ensure that all systems maintain consistent configurations and security settings.

### Objectives

* Demonstrate centralized system administration using automation tools
* Reduce manual system configuration tasks
* Ensure consistent configuration across multiple machines
* Implement policy‑based system management
* Provide a virtual environment to test infrastructure automation

### Target Users

* System administrators
* DevOps engineers
* IT students learning infrastructure automation
* Small organizations managing multiple Linux machines

---

## System Architecture / Design

The system follows a **Controller–Client architecture**.

### Components

1. **Controller Node**

   * Central machine responsible for automation
   * Runs Ansible and executes playbooks
   * Stores inventory and policy definitions

2. **Client Nodes**

   * Managed machines in the network
   * Receive configuration commands from the controller
   * Execute tasks such as software installation and service configuration

3. **Automation Engine**

   * Implemented using Ansible
   * Executes playbooks and roles to enforce policies

4. **Secure Communication Layer**

   * SSH used for remote communication
   * SSH key authentication used for password‑less automation

### Workflow

1. Administrator defines policies using Ansible playbooks
2. Controller reads the inventory of client machines
3. Controller connects to clients via SSH
4. Playbooks execute tasks on remote machines
5. Client machines apply configurations automatically

---

## Technologies Used

### Programming / Scripting

* Python
* YAML
* Bash

### Automation Tools

* Ansible

### Virtualization

* VirtualBox

### Operating System

* Lubuntu / Ubuntu Linux

### Network Tools

* SSH (Secure Shell)

### Version Control

* Git
* GitHub / GitLab / Bitbucket

---

## Installation Instructions

### Requirements

* VirtualBox installed
* Linux ISO (Lubuntu/Ubuntu)
* Minimum 8GB RAM recommended
* Internet connection

### Step 1: Create Virtual Machines

Create the following virtual machines:

* Controller VM
* Client VM 1
* Client VM 2
* Client VM 3

All machines should be connected to the same internal network.

### Step 2: Install Required Packages

Run the following on each client machine:

```
sudo apt update
sudo apt install openssh-server python3 -y
```

### Step 3: Setup SSH Authentication

On the controller machine:

```
ssh-keygen
ssh-copy-id user@client-ip
```

This enables password‑less SSH access.

### Step 4: Install Ansible (Controller Only)

```
sudo apt update
sudo apt install ansible -y
```

### Step 5: Create Project Workspace

```
mkdir ~/autosanp
cd ~/autosanp
```

---

## Usage Instructions

### 1. Create Inventory File

Example `inventory.ini`:

```
[clients]
192.168.10.20
192.168.10.21
192.168.10.22
```

### 2. Test Connectivity

```
ansible -i inventory.ini all -m ping
```

Expected Output:

```
pong
```

### 3. Run Automation Playbook

Example command:

```
ansible-playbook -i inventory.ini install_apache.yml
```

This automatically installs Apache web server on all client machines.

---

## Dataset

This project does not use a dataset. The system operates on virtual machines within a simulated network environment.

---

## Project Structure

```
autosanp/
│
├── app/
|   ├── app.py
│   ├── dashboard.py  
├── data/
|   ├── autosanp_logs.json
│   ├── host.ini 
├── logs/
├── policies/
│   ├── database_policy.yml
|   ├── network_policy.yml
│   ├── security_policy.yml
│   ├── server_policy.yml
├── secrets/
└── README.md
```

---

## Screenshots / Demo

Suggested screenshots to include:

* VirtualBox virtual network setup
* SSH connection from controller to client
* Ansible ping test
* Playbook execution results
* Apache web server running on client

A short demo video showing the automation process can also be included.

---

## Contributors

| Name        | Role                                             |
| ----------- | ------------------------------------------------ |
|   P.N Maleesha Dilshan   | Virtual environment setup and Ansible automation |
|     Tharindu Sampath     | Network configuration and system connectivity    |
|   H.A.S.R.H. Arachchi    | Automation playbook development                  |
| H.D.T.R. Abhayawardhana  | Automation policy implementation and testing     |
|   D.M.H.I. Balasooriya   | System architecture and repository management    |

---

## Contact Information

Institution: University Project Team

For questions or collaboration, contact any team member via the emails listed in the project documentation.

---

## License

This project is released for educational purposes.

Suggested license:

MIT License

You may reuse and modify the project with proper attribution.
=======
# autosanp
