# Valued delivery slip

- This module is used to manage  the cloud instances for all our customers.

**Table of Contents**

- Features
- Configuration
- Usage
- Dependencies

---

## Features

- New menuitem "insatnce cloud" added under 
- A button "instance" added in the form view to generate the instance of each project.
- In this module, there are two menus: Instances and Configuration.
- Under the Configuration menu, you can access to the view form for the Odoo Version,Operating System,and Hosting Provider models.
- A warning message appears when you click at the password icon 
- Two new groups are created : "Administrator instance" and "user instance" .
- This module is available in both languages French and English .

---

## Configuration

No configuration needed.

---

## Usage

1. Go to application list & install `v__cloud_instances_manager` module.

---

## Dependencies

### Odoo modules dependencies

| Module      | Why used?                                                                                          | Side effects |
|-------------|----------------------------------------------------------------------------------------------------|--------------|
| project     | Needed to see the project that use this server and to access to the instances used by this project |              |
| hr          | Employee who installed Odoo.                                                                       |              |
| res.partner | the client                                                                                         |              |
