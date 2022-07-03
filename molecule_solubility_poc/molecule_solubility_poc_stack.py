from aws_cdk import (
    # Duration,
    Stack,
    aws_ecr as ecr
)
from constructs import Construct

class MoleculeSolubilityPocStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ecr_repository = ecr.Repository(
            self,
            id=' molecule_solubility_ecr_repository',
            repository_name='molecule_solubility_repository'
        )
