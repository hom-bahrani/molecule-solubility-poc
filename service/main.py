from fastapi import FastAPI, Request
import boto3
import os
import deepchem as dc
import h5py

app = FastAPI(title="Molecule Solubility Service")


@app.get("/")
def get_message():
    return {"message": "hello..."}

@app.post("/train")
async def get_message(request: Request):
    
    body = await request.json()
    url = body['url']
    s3_bucket_name = body['bucketName']
    
    filename = 'delaney-processed.csv'
    
    tasks, datasets, transformers = dc.molnet.load_delaney(featurizer='GraphConv')
    train_dataset, valid_dataset, test_dataset = datasets

    # Create and train the model.
    model = dc.models.GraphConvModel(n_tasks=1, mode='regression', dropout=0.2)
    model.fit(train_dataset, nb_epoch=150)

    # Evaluate it.
    metric = dc.metrics.Metric(dc.metrics.pearson_r2_score)
    print("Training set score")
    print(model.evaluate(train_dataset, [metric], transformers))
    print("Test set score")
    print(model.evaluate(test_dataset, [metric], transformers))
    
    # save model
    print("Saving model")
    print(model.summary())
    model.save('molecule_solubility.h5')
    
    # upload to S3
    s3_path = f'models/{filename}'
    s3 = boto3.resource("s3")
    s3.Object(s3_bucket_name, s3_path).put(Body=open('molecule_solubility.h5', 'rb'))

@app.post("/predict")
async def get_message(request: Request):
    body = await request.json()
    print(body['url'])
    print(body['bucketName'])
    return body
