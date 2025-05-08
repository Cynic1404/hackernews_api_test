from api_helpers.api_helpers import ApiHelpers
from api.hacker_news_apis import HackerNewsAPI
import random
import pytest
import time
from test_helpers.test_helpers import (
    validate_comment_common_fields,
    validate_deleted_comment,
    validate_dead_comment,
    validate_story_fields
)

class TestPrintTopStories:

    def test_get_top_comment_to_the_top_story(self):
        top_story_id = ApiHelpers.get_the_top_story()
        if comments:=ApiHelpers.get_list_of_comments_to_story(top_story_id):
            top_comment_id=comments[-1]
            response = HackerNewsAPI.get_item(top_comment_id)
            assert response["type"] == "comment"
            assert response["parent"] == top_story_id
            assert isinstance(response["text"], str)
        else:
            pytest.skip("No comments found for selected story.")

    def test_nonexistent_item_id_returns_none(self):
        response = HackerNewsAPI.get_item(999999999999)
        assert response is None

    @pytest.mark.parametrize("wrong_id", ["a"," ", "", "%"])
    def test_check_item_api_with_wrong_url(self, wrong_id):
        response = HackerNewsAPI.get_item(wrong_id)
        if wrong_id == "":
            assert response == {'error': 'Permission denied'}
        else:
            assert not response

    def test_item_api_returns_valid_comment_and_story_structure(self):
        random_story = random.choice(ApiHelpers.get_top_stories_list())
        story_data = HackerNewsAPI.get_item(item_id=random_story)
        comments = story_data.get("kids")

        if not comments:
            items_to_check = [random_story]
        else:
            random_comment = random.choice(comments)
            items_to_check = [random_story, random_comment]

        for item in items_to_check:
            response = HackerNewsAPI.get_item(item_id=item)
            assert "id" in response and isinstance(response["id"], int)
            assert "type" in response and isinstance(response["type"], str)

            if response["type"] == "story":
                validate_story_fields(response)

            elif response["type"] == "comment":
                validate_comment_common_fields(response)
                if response.get("deleted") or response.get("dead"):
                    continue
                else:
                    assert "parent" in response and isinstance(response["parent"], int)
                    assert "text" in response and isinstance(response["text"], str)


    def test_deleted_comment_structure(self):
        deleted_comment_id = 43920636
        response = HackerNewsAPI.get_item(deleted_comment_id)
        validate_comment_common_fields(response)
        validate_deleted_comment(response)


    def test_dead_comment_structure(self):
        dead_comment_id = 43894689
        response = HackerNewsAPI.get_item(dead_comment_id)
        validate_comment_common_fields(response)
        validate_dead_comment(response)


    def test_get_item_with_and_without_print_pretty_returns_same_result(self):
        random_story = random.choice(ApiHelpers.get_top_stories_list())
        pretty_list = HackerNewsAPI.get_item(random_story, print_pretty=False)
        not_pretty_list = HackerNewsAPI.get_item(random_story)
        assert pretty_list==not_pretty_list

    def test_item_response_time_is_acceptable(self):
        random_story = ApiHelpers.get_the_top_story()
        start = time.time()
        _ = HackerNewsAPI.get_item(random_story)
        elapsed = time.time() - start
        assert elapsed < 2.0