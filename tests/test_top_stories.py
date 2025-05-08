from api_helpers.api_helpers import ApiHelpers
from api.hacker_news_apis import HackerNewsAPI

class TestPrintTopStories:

    def test_top_stories_list_content(self):
        top_stories_list = ApiHelpers.get_top_stories_list()
        assert 0 < len(top_stories_list) <= 500
        assert all(isinstance(story_id, int) for story_id in top_stories_list)

    def test_top_stories_with_and_without_print_pretty_returns_same_result(self):
        pretty_list = HackerNewsAPI.get_top_stories(print_pretty=False)
        not_pretty_list = HackerNewsAPI.get_top_stories()
        assert pretty_list==not_pretty_list



