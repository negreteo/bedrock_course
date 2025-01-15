import boto3;
import pprint;

bedrock = boto3.client(service_name='bedrock')

pp = pprint.PrettyPrinter(depth=4)

def list_foundations_models():
    models = bedrock.list_foundation_models()

    for model in models["modelSummaries"]:
        pp.pprint(model)
        pp.pprint("--------------")


def get_foundation_model(modelIdentifier):
    model = bedrock.get_foundation_model(modelIdentifier=modelIdentifier)
    pp.pprint(model)

list_foundations_models()
# get_foundation_model('anthropic.claude-v2')