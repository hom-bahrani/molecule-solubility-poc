# Molecule Solubility POC

The goal of this POC is to use machine learning to predict how easily a molecule dissolves in water. 

Solubility is a really important property for any chemical that we want to use as a drug. If the molecule doesn't dissolve easily, getting enough of it into a patient’s bloodstream to have a therapeutic effect will be really difficult, if not impossible. 

Scientists therefore spend a lot of time modifying molecules to try to increase their solubility, and having a model that can predict this may save them some time in the lab. 

<img width="836" alt="Screenshot 2022-07-04 at 22 15 23" src="https://user-images.githubusercontent.com/8465628/177218294-569736e9-349e-43a0-918e-90a5520fdc2e.png">

The POC uses a deep learning model that is deployed to a Fargate container in AWS. A very basic python service trains the model and  can then predict the solubility of molecules passed in as a `SMILES` string.

SMILES is a popular method for codifying molecules as text strings. A SMILES string describes the atoms and bonds of a molecule in a way that is both concise and reasonably intuitive to chemists. To nonchemists, these strings tend to look like meaningless patterns of random characters. For example, “OCCc1c(C)[n+] (cs1)Cc2cnc(C)nc2N” describes the important nutrient thiamine, also known as vita‐ min B1.

One thing to bear in mind is that in this is just an example and the data has already been cleaned and processed (see data directory) ready for the model. In a practical environment we would need to build a data pipeline to pre-process and clean the molecule data before its ready for the ML model training phase.


## Deploying to AWS

```
$ python3 -m venv .venv
```

Once you have set up your AWS credentials you are ready to deploy the project.

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
$ cdk deploy
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Running FastAPI locally

To run the training/prediction service locally:

```bash
cd service

pip install -r requirements.txt

uvicorn main:app --host 0.0.0.0 --port 8080
```

Alternatively if you have docker set up, you build the docker image and run that.
