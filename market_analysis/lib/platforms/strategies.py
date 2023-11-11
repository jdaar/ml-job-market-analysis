from enum import Enum
from pyppeteer import launch

from .base_strategy import AbstractStrategy
from .utils import retrieve_proxy

class LinkedinStrategy(AbstractStrategy):
    @staticmethod
    async def run(lines) -> dict:
        proxy = retrieve_proxy()
        print(f"Using proxy: {proxy}")
        browser = await launch(
            {
                "executablePath": "/usr/bin/chromium-browser",
                "args": [
                    "--no-sandbox",
                    "--disable-setuid-sandbox",
                    "--disable-web-security",
                    "--disable-dev-profile",
                    f"--proxy-server={proxy.host}:{proxy.port}",
                ],
                "headless": True,
            }
        )
        pages = [await browser.newPage() for idx in range(0, len(lines))]

        for idx, page in enumerate(pages):
            await page.goto(lines[idx]["url"])
            await page.screenshot({"path": f"/output/{lines[idx]['uuid']}.png"})

        await browser.close()


class Platforms(Enum):
    Linkedin = "linkedin"


PlatformStrategies = {
    Platforms.Linkedin: LinkedinStrategy,
}
