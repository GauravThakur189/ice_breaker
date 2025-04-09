from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name: str) -> str:
    """
    Get the LinkedIn profile URL using Tavily Search.
    Args:
        name (str): The name of the person.
    Returns:
        str: The LinkedIn profile URL.
    """
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res