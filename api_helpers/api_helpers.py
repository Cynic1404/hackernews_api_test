from api.hacker_news_apis import HackerNewsAPI

class ApiHelpers:

    @classmethod
    def get_top_stories_list(cls):
        return HackerNewsAPI.get_top_stories()

    @classmethod
    def get_the_top_story(cls):
        return HackerNewsAPI.get_top_stories()[-1]

    @classmethod
    def get_list_of_comments_to_story(cls, story_id):
        return HackerNewsAPI.get_item(story_id).get("kids")



