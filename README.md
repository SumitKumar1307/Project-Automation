**Installation**

Follow these steps to run this script:
```bash
$ git clone https://github.com/SumitKumar1307/Project-Automation.git
$ cd Project-Automation
$ pip install -r requirements.txt
$ chmod +x new_project config
```

**Configuration**

```bash
$ ./config
```
Enter your Github Access Token with at-least the following permissions: repo, user

**Usage**
Using the script is really simple, you just have to do:

```bash
$ ./new_project <project_name>
```
**TroubleShooting**
If you run into any then here are a few things to try out:

1. A repository with your project name does not already exists for your accout.
2. You Have Git Installed.
3. Run ./config if you haven't already done that.
4. Make sure that you have made both new_project and config files executable, if not then the steps are mentioned in Installation.
```
