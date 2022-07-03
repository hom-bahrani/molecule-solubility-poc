import aws_cdk as core
import aws_cdk.assertions as assertions

from molecule_solubility_poc.molecule_solubility_poc_stack import MoleculeSolubilityPocStack

# example tests. To run these tests, uncomment this file along with the example
# resource in molecule_solubility_poc/molecule_solubility_poc_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MoleculeSolubilityPocStack(app, "molecule-solubility-poc")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
