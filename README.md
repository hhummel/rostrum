# <img alt="rostrum on a platform" width="30px" src="https://qph.cf2.quoracdn.net/main-qimg-ae798e187d82561d5e98a8802a57bc30-lq" /> Welcome to Rostrum!

Rostrum is small platform that sits on a larger platform for CDK development with Python. It's like when they open a Starbuck's inside of a Starbuck's.

The plan is to use tools created by or recommended by the HealthVerity Platform stack to implement services that other applications or services can register for and consume. For demo purposes we'll be making a cron service. The primary goal is to get more comfortable and confident in how to use the Platform technology. If a useful service comes out of it that's a bonus.

This repo uses Python, but the native language for the CDK is Typecript. A possible next step would be to complete a similar exercise in Typescript and see if it's easier or clearer or otherwise superior.

## Some potentially useful boilerplate

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project. The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory. To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

- `cdk ls` list all stacks in the app
- `cdk synth` emits the synthesized CloudFormation template
- `cdk deploy` deploy this stack to your default AWS account/region
- `cdk diff` compare deployed stack with current state
- `cdk docs` open CDK documentation

Enjoy!
