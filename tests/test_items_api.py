from http.client import responses

from api_helpers.api_helpers import ApiHelpers
from api.hacker_news_apis import HackerNewsAPI
import random
import pytest

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
                assert "title" in response and isinstance(response["title"], str)
                assert "by" in response and isinstance(response["by"], str)
                if "url" in response:
                    assert isinstance(response["url"], str)
                if "text" in response:
                    assert isinstance(response["text"], str)
                if "score" in response:
                    assert isinstance(response["score"], int)
                if "descendants" in response:
                    assert isinstance(response["descendants"], int)

            elif response["type"] == "comment":
                assert "parent" in response and isinstance(response["parent"], int)
                assert "by" in response and isinstance(response["by"], str)
                if "text" in response:
                    assert isinstance(response["text"], str)
                if "deleted" in response:
                    assert isinstance(response["deleted"], bool)
                if "dead" in response:
                    assert isinstance(response["dead"], bool)


    def test_get_item_with_and_without_print_pretty_returns_same_result(self):
        random_story = random.choice(ApiHelpers.get_top_stories_list())
        pretty_list = HackerNewsAPI.get_item(random_story, print_pretty=False)
        not_pretty_list = HackerNewsAPI.get_item(random_story)
        assert pretty_list==not_pretty_list