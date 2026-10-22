import scraper
HTML = """<html><body><article class="product_pod"><p class="star-rating Three"></p>
<h3><a href="a-book_1/index.html" title=" A Book ">A Book</a></h3><p class="price_color">Â£51.77</p>
<p class="availability">In stock</p></article><ul class="pager"><li class="next"><a href="page-2.html">next</a></li></ul></body></html>"""

def test_parse():
    rows, nxt = scraper.parse_page(HTML, "https://books.toscrape.com/catalogue/page-1.html")
    assert rows[0] == {"title": "A Book", "price_gbp": 51.77, "rating": 3, "in_stock": True,
                       "url": "https://books.toscrape.com/catalogue/a-book_1/index.html"}
    assert nxt.endswith("page-2.html")

def test_dedupe():
    r = {"url": "x"}; assert len(scraper.dedupe([r, dict(r), {"url": "y"}])) == 2

class FakeResp:
    def __init__(s, html, url): s.content, s.url = html.encode(), url
    def raise_for_status(s): pass

class FakeSess:
    def get(s, url, timeout): return FakeResp(HTML.replace('<li class="next"><a href="page-2.html">next</a></li>', "") if "page-2" in url else HTML, url)

def test_pagination_offline():
    rows, n = scraper.scrape(sess=FakeSess(), delay=0)
    assert n == 2 and len(scraper.dedupe(rows)) == 1
