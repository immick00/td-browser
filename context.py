import uuid
from patchright.async_api import Browser, BrowserContext

from utilities import get_random_timezone, get_random_resolution, inject_browser_js, get_random_gpu
import random

with open("script.js", "r", encoding="utf-8") as f:
    script_content = f.read()

class ChromeContext:
    def __init__(self, browser: Browser):
        self.id = uuid.uuid4()
        self.browser: Browser = browser
        self.timezone = get_random_timezone()
        self.context = None
        self.page = None

    def get_browser(self):
        return self.browser

    async def initialize_context(self, proxy: str = None):
        context_options = {}

        if proxy:
            proxy_parts = proxy.split(':')
            if len(proxy_parts) >= 2:
                proxy_address = f"{proxy_parts[0]}:{proxy_parts[1]}"
                context_options = {
                    'proxy': {
                        'server': f"http://{proxy_address}",
                    }
                }
                if len(proxy_parts) == 4:
                    proxy_username = proxy_parts[2]
                    proxy_password = proxy_parts[3]
                    context_options["proxy"]["username"] = proxy_username
                    context_options["proxy"]["password"] = proxy_password

        resolution = get_random_resolution()
        # Make viewport a bit smaller than our available resolution
        viewport_width = int(random.uniform(0.5 * resolution["width"], 0.85 * resolution["width"]))
        viewport_height = int(random.uniform(0.5 * resolution["height"], 0.85 * resolution["height"]))

        context_options["viewport"] = {"width": viewport_width, "height": viewport_height}
        context_options["screen"] = {"width": resolution["width"], "height": resolution["height"]}

        context_options["timezone_id"] = self.timezone

        if self.browser is None:
            raise RuntimeError("Browser is not initialized")

        try:
            context: BrowserContext = await self.browser.new_context(**context_options)
            await inject_browser_js(context, resolution["width"], resolution["height"])
            self.context = context
            return context
        except Exception as e:
            raise e

    async def start(self):
        page = await self.context.new_page()
        gpu_str = get_random_gpu()

        modified_script = script_content.replace("GPU_VENDOR_RENDERER_HERE", gpu_str)

        async def handle_route(route, request):
            if "fm.js" in request.url and request.method == "GET":
                await route.fulfill(status=200, content_type="application/javascript", body=modified_script)
            else:
                await route.continue_()

        await page.route("**/*", handle_route)
        await page.goto(f"https://www.popmart.com/ca", wait_until=None)
        self.page = page

    async def get_fingerprint(self):
        return await self.page.evaluate("() => window.getFingerprint()", isolated_context=False)

    async def get_user_agent(self):
        return await self.page.evaluate("navigator.userAgent")

    async def decode_result(self, request_id, result):
         return await self.page.evaluate("([requestId, result]) => window.decodeResult(requestId, result)", [request_id, result], isolated_context=False)

    async def get_session_key(self, token_id):
        return await self.page.evaluate("([tokenId]) => window.getSessionKey(tokenId)", [token_id], isolated_context=False)

    async def get_session_sign(self, path, body):
        td_session = await self.page.evaluate('([path, body]) => window._fmOpt.sign({path: path, body: body })', [path, body],
                                         isolated_context=False)
        return td_session['sign']





