# SSSD AD group policy test

The goal is to check if the access control based on AD group policy
works as expected.


## Scenario

The test creates 3 GPOs which are expected to

- grant login access only to a particular user and administrators
- deny login access to a particular user
- both grant login access only to a particular user and administrators, and
  deny login access to the same user (the resulting policy would allow login
  access to administrators only)

Each GPO is linked to its own OU (so there are 3 OUs). The test moves client
machines to these OUs (so the test needs at least 3 client machines).
The test logs in to every client machine (from the domain controller) and
checks if the actual result (login granted/denied) matches the expectation.


## Prerequisites

* 4 hosts in the same L2 network 
  - every host runs ALT Linux (p8)
  - exactly 1 of the hosts is the domain controller
  - 3 hosts are clients
* passwordless ssh root access to these hosts (presumably via public
  key authentication)
* Control machine
  - running Linux
  - able to connect to the test hosts via ssh


## Preparations

1. Install ansible and git on the control machine. On ALT Linux run
   ```bash
   sudo apt-get install -y ansible git
   ```

2. Clone this repository
   ```bash
   git clone --recursive git://git.altlinux.org/people/asheplyakov/public/sssd-gpo-ftests.git
   cd sssd-gpo-ftests
   ```

3. Adjust the **hosts.sample** file and rename it to **hosts**

4. Adjust the **group_vars/all.yml.sample** file and rename it to **group_vars/all.yml**

5. Check if the test hosts are reachable via ssh

   ```bash
   ansible -i hosts -m ping all
   ```
   If some hosts are not reachable fix connection issues before continuing


## Running the test

```bash
ansible-playbook -i hosts setup.yml
```
