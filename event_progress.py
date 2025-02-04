from tortoise import fields
from tortoise.models import Model


class EventProgressModel(Model):
    id = fields.BigIntField(pk=True)
    init_block_height = fields.BigIntField()
    last_block_height = fields.BigIntField()
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "event_progress"
