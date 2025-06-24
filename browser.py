from typing import List

import uuid
from patchright.async_api import  async_playwright

from context import ChromeContext


class ChromeBrowser:
    def __init__(self, contexts_per_browser: int):
        self.id = uuid.uuid4()
        self.contexts_per_browser = contexts_per_browser
        self.contexts: List[ChromeContext] = []
        self.browser = None

    async def create_chrome_instance(self):
        args = [
            "--disable-blink-features=AutomationControlled",
            '--webrtc-ip-handling-policy=disable_non_proxied_udp',
            '--force-webrtc-ip-handling-policy',
        ]

        p = await async_playwright().start()
        browser = await p.chromium.launch(args=args, headless=False, channel="chrome")
        self.browser = browser

    def create_contexts(self):
        for _ in range(self.contexts_per_browser):
            c = ChromeContext(self.browser)
            self.contexts.append(c)

    async def initialize_contexts(self):
        for context in self.contexts:
            await context.initialize_context()
            await context.start()

