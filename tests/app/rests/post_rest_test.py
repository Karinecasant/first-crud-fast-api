import pytest
from http import HTTPStatus

pytestmark = [pytest.mark.asyncio]

@pytest.mark.usefixtures("clear_post_database")
async def test_should_create_post(client, post_prefix):
    res = await client.get(post_prefix)

    posts = res.json()
    assert len(posts) == 0

    res = await client.post(post_prefix, json={
        "title":"test",
        "author":"me",
        "content":"test2"
    })
    assert res.status_code == HTTPStatus.OK
    
    post = res.json()
    assert "id" in post

    res = await client.get(post_prefix)

    posts = res.json()
    assert len(posts) == 1
    assert posts[0]["id"] == post["id"]
    assert posts[0]["title"] == post["title"]
    assert posts[0]["author"] == post["author"]
    assert posts[0]["content"] == post["content"]



