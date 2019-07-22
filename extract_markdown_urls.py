import markdown
from lxml import etree

from pathlib import Path

dir = '/home/bradleybossard/src/cheatsheets/reading-lists'
pattern = '**/*.md'

for filename in Path(dir).glob(pattern):
    with open(filename, 'r') as file:
        body_markdown = file.read()
        html = markdown.markdown(body_markdown)
        html = '<html>' + html + '</html>'
        doc = etree.fromstring(html)
        for link in doc.xpath('//a'):
            print(link.get('href'))

