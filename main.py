import re
import time
import urllib.request

from msedge.selenium_tools import Edge, EdgeOptions

import configs as configs


def extract_element():
    options = EdgeOptions()
    options.headless = True
    options.use_chromium = True

    driver = Edge(executable_path=configs.msedge_driver_executable_path, options=options)
    driver.get(configs.home_page_url)
    time.sleep(4)

    element = driver.find_element_by_xpath(configs.html_image_element)
    html = element.get_attribute('outerHTML')
    driver.quit()
    return html


def extract_image_url(html: str):
    found = re.search(r"url\(.*\)", html).group()
    return found.replace('url(&quot;', '').replace('&quot;)', '')


def save_image(image_url: str):
    print(f'image_url: {image_url}')
    urllib.request.urlretrieve(image_url, "image.jfif")


extracted_element = extract_element()
extracted_image_url = extract_image_url(extracted_element)
save_image(extracted_image_url)
