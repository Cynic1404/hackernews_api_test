def validate_comment_common_fields(response):
    assert response.get("type") == "comment"
    assert "id" in response and isinstance(response["id"], int)

def validate_deleted_comment(response):
    assert response.get("deleted") is True
    assert "text" not in response
    assert "by" not in response

def validate_dead_comment(response):
    assert response.get("dead") is True
    assert "by" in response and isinstance(response["by"], str)
    assert "text" in response and response["text"] == "[flagged]"
    assert "parent" in response and isinstance(response["parent"], int)
    assert "kids" in response and isinstance(response["kids"], list)

def validate_story_fields(response):
    assert response["type"] == "story"
    assert "title" in response and isinstance(response["title"], str)
    assert "by" in response and isinstance(response["by"], str)