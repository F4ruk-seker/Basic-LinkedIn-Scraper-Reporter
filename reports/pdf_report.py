import config
import asyncio
from pyppeteer import launch


async def generate_pdf_from_html(html_content, pdf_path):
    browser = await launch(executablePath=config.CHROME_PATH)
    page = await browser.newPage()
    await page.setContent(html_content)
    await page.addStyleTag(url=config.BOOTSTRAP_CDN)
    await asyncio.sleep(2)
    await page.pdf({'path': pdf_path, 'format': 'A4'})
    await browser.close()
