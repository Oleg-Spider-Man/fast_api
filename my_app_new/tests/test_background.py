import pytest


@pytest.mark.asyncio
async def test_get_email(aclient):
    # должен быть включен redis
    response = await aclient.get('/email/')
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_notification(aclient):
    response = await aclient.post('/send-notification/email@email')
    assert response.status_code == 200
