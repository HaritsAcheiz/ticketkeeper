from selenium.webdriver import ActionChains, Keys
from seleniumbase import SB
from dataclasses import dataclass
import os
from dotenv import load_dotenv
import random


load_dotenv()

@dataclass
class TicketKeeper():
    base_url: str = 'https://www.ticketswap.com/'

    def login(self, sb):
        sb.driver.uc_open_with_tab(self.base_url)
        while 1:
            try:
                # sb.driver.uc_click('button:contains(Click)')
                # sb.sleep(random.uniform(1, 2))
                xoffset = random.randint(0, 50)
                yoffset = random.randint(0, 50)
                sb.click_with_offset('button:contains(Click)', xoffset, yoffset, timeout=3)
                # sb.sleep(random.uniform(1, 2))
                input('Solve captcha then press any key!!!')
                # style = sb.find_element('button:contains(Click)').attribute.get('style').split(";")
                # sb.click
            except Exception as e:
                print(e)
                break
        sb.click('button:contains(Log)', timeout=3)
        sb.click('input#email', timeout=3)
        sb.update_text('input#email', f"{os.getenv('USER')}")
        sb.click('button:contains(Continue)', timeout=3)
        sb.click('input[type="email"]', timeout=3)
        sb.update_text('input[type="email"]', f"{os.getenv('USER')}")
        sb.click('button:contains(Next)', timeout=3)
        sb.click('input[type="password"]', timeout=3)
        sb.update_text('input[type="password"]', f"{os.getenv('PASS')}")
        sb.click('button:contains(Next)', timeout=3)
        sb.click('button:contains(Continue)', timeout=3)
        # sb.sleep(10)
        sb.switch_to_window(sb.driver.window_handles[0])
        # sb.save_cookies('cookies.txt')

    def order(self, sb, keyword):
        try:
            sb.send_keys('input#site-search', keyword)
            sb.sleep(1)
            sb.send_keys('input#site-search', Keys.RETURN)
            sb.click('div#__next > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(1) > a', timeout=3)
            sb.click('ul[data-testid="event-types-list"] > li > a', timeout=3)
            sb.click('a[data-testid="listing"]', timeout=3)
            sb.click('button:contains(Buy)', timeout=3)
            sb.click('button:contains(Continue)', timeout=3)
            sb.click('button:contains(cart)', timeout=3)
            sb.sleep(20)
        except Exception as e:
            print(e)
            sb.sleep(1000)

    def main(self, keyword):
        with SB(uc=True, test=False, incognito=True, maximize=True, page_load_strategy='eager') as sb:
            self.login(sb)
            self.order(sb, keyword)

if __name__ == '__main__':
    keyword = input("Please type ticket search keyword:")
    driver = TicketKeeper()
    driver.main(keyword)