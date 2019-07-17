import markdown
from lxml import etree

body_markdown = "This is an [inline link](http://google.com). This is a [non inline link][1]\r\n\r\n  [1]: http://yahoo.com"

doc = etree.fromstring(markdown.markdown(body_markdown))
for link in doc.xpath('//a'):
    print(link.text, link.get('href'))
