import feedparser
import xml.etree.ElementTree as ET
from urllib.parse import quote



def news_feed_html():
    feed = feedparser.parse('https://www.ekonomidunya.com/rss_ekonomi_1.xml')

    html_content = ""
    print('printing news:')
    subject = 'Ekonomi'
    for item in feed.entries[0:3]:
        title = item.title
        length = len(item.title)
        source_url = 'google.com'
        description = item.description[length+1:]
        image_src = item.links[0]['href']
        date = item.published
        href = f"single.html?title={quote(title)}&description={quote(description)}&image_src={quote(image_src)}&source_url={quote(source_url)}&date={quote(date)}&subject={quote(subject)}"
        html_content += f"""
        <div class="position-relative overflow-hidden" style="height: 500px;">
            <img class="img-fluid h-100" src="{image_src}" style="object-fit: cover;">
            <div class="overlay">
                <div class="mb-2">
                    <a class="badge badge-danger text-uppercase font-weight-semi-bold p-2 mr-2">{subject}</a>
                    <a class="text-white">{date}</a>
                </div>
                <a class="h2 m-0 text-white text-uppercase font-weight-bold" href={href}>{title}</a>
            </div>
        </div>
        """
    return html_content

news_feed_html()