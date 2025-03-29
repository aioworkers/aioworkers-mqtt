from uuid import uuid4

import pytest

from aioworkers_mqtt.paho import Storage


@pytest.fixture
def config_yaml():
    return """
    storage:
        cls: aioworkers_mqtt.Storage
        # host: 127.0.0.1
        port: 1883
        client_id: w
        # protocol: 5
        qos: 2
        retain: true
        prefix: pref
        format: json
    """


@pytest.mark.asyncio
async def test_storage(context):
    s: Storage = context.storage
    topic = str(uuid4())
    data = {"data": str(uuid4())}
    await s.set(topic, data)
    dt = await s.get(topic)
    assert dt == data
