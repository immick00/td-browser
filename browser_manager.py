import random

from browser import ChromeBrowser
from context import ChromeContext
from typing import List

with open("script.js", "r", encoding="utf-8") as f:
    script_content = f.read()

class BrowserManager:
    def __init__(self, concurrent_browsers: int, contexts_per_browser: int):
        self.concurrent_browsers = concurrent_browsers
        self.contexts_per_browser = contexts_per_browser
        self.browsers: List[ChromeBrowser] = []

    async def initialize(self):
        for i in range(self.concurrent_browsers):
            cb = ChromeBrowser(contexts_per_browser=self.contexts_per_browser)

            await cb.create_chrome_instance()
            cb.create_contexts()
            await cb.initialize_contexts()
            self.browsers.append(cb)

    def get_random_context(self) -> ChromeContext:
        random_browser: ChromeBrowser = random.choice(self.browsers)
        random_context: ChromeContext = random.choice(random_browser.contexts)
        return random_context

    def get_all_contexts(self) -> List[ChromeContext]:
        contexts: List[ChromeContext] = []

        for browser in self.browsers:
            for context in browser.contexts:
                contexts.append(context)
        return contexts

    def get_context_by_id(self, context_id: str) -> ChromeContext:
        contexts = self.get_all_contexts()
        for context in contexts:
            if str(context.id) == context_id:
                return context
        raise Exception("context id not found")