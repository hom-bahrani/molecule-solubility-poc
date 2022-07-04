from aws_cdk import (
    # Duration,
    Stack,
    aws_ecr as ecr,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
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
        
        cluster = ecs.Cluster(self, 'molecule_solubility_EcsCluster')
        
        task_definition = ecs.FargateTaskDefinition(self, 
                                                    'MoleculeSolubilityDemoServiceTask', 
                                                    family='MoleculeSolubilityDemoServiceTask')
        
        image = ecs.ContainerImage.from_asset('service')
        
        container = task_definition.add_container('molecule_solubility_app', image=image)
        container.add_port_mappings(ecs.PortMapping(container_port=8080))

        ecs_patterns.ApplicationLoadBalancedFargateService(self, 'molecule_solubility_Service',
                                                           cluster=cluster,
                                                           desired_count=1,
                                                           task_definition=task_definition)
        
        
