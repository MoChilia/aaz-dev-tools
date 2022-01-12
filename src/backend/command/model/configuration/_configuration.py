from schematics.models import Model
from schematics.types import ModelType, ListType
from utils.fields import PlaneField

from ._command_group import CMDCommandGroup
from ._resource import CMDResource


class CMDConfiguration(Model):
    # properties as nodes
    plane = PlaneField(required=True)

    resources = ListType(ModelType(CMDResource), min_size=1, required=True)  # resources contained in configuration file
    command_group = ModelType(
        CMDCommandGroup,
        serialized_name='commandGroups',
        deserialize_from='commandGroups',
    )

    class Options:
        serialize_when_none = False
