import socks
import socket

import stem.process

SOCKS_PORT=

tor_process = stem.process.launch_tor_with_config(
    config = {
        'SocksPort': str(SOCKS_PORT),
    },
)


socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5,
                      addr="py-learn.vercel.app", #theres a ',' change it to '.' -- linkedin was being glitchy
                      port=SOCKS_PORT)
socket.socket = socks.socksocket




#Write your scraping code here -- I use BeautifulSoup for scraping




tor_process.kill()
