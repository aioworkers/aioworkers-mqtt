from uuid import uuid4

import pytest

from aioworkers_mqtt.paho import Queue


@pytest.fixture
def config_yaml():
    return f"""
    queue:
        cls: aioworkers_mqtt.Queue
        # host: 127.0.0.1
        port: 1883
        client_id: w
        # protocol: 5
        qos: 2
        retain: false
        topics: [{uuid4()}]
        format: json
    """


@pytest.mark.asyncio
async def test_queue(context):
    q: Queue = context.queue
    data = {"data": str(uuid4())}
    await q.put(data)
    dt = await q.get()
    assert dt == data
