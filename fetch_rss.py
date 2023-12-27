import feedparser
import xml.etree.ElementTree as ET
from urllib.parse import quote


def fetch_news():
    news = feedparser.parse('https://www.ekonomidunya.com/rss_ekonomi_1.xml')
    return news


def news_feed_html():
    feed = fetch_news()
    subject = 'Ekonomi'
    main_news_item = feed.entries[0]
    title = main_news_item.title
    length = len(main_news_item.title)
    source_url = main_news_item.link
    description = main_news_item.description[length+1:]
    content = main_news_item.content[0]['value']
    image_src = main_news_item.links[0]['href']
    date = main_news_item.published
    href = f"single.html?title={quote(title)}&description={quote(description)}&image_src={quote(image_src)}&source_url={quote(source_url)}&date={quote(date)}&subject={quote(subject)}&content={quote(content)}"
    main_html_content = f"""
    <div class="position-relative overflow-hidden" style="height: 500px;">
        <img class="img-fluid w-100 h-100" src={image_src} style="object-fit: cover;">
        <div class="overlay">
            <div class="mb-2">
                <a class="badge badge-danger text-uppercase font-weight-semi-bold p-2 mr-2">{subject}</a>
                <a class="text-white">{date}</a>
            </div>
            <a class="h6 m-0 text-white text-uppercase font-weight-semi-bold" href={href}>{title}</a>
        </div>
    </div>
    """
    secondary_html_content = ""
    remaining_html_content = ""
    print('printing news:')
    for item in feed.entries[1:5]:
        title = item.title
        length = len(item.title)
        source_url = item.link
        description = item.description[length+1:]
        content = item.content[0]['value']
        image_src = item.links[0]['href']
        date = item.published
        href = f"single.html?title={quote(title)}&description={quote(description)}&image_src={quote(image_src)}&source_url={quote(source_url)}&date={quote(date)}&subject={quote(subject)}&content={quote(content)}"
        secondary_html_content += f"""
            <div class="col-md-6 px-0">
                <div class="position-relative overflow-hidden" style="height: 250px;">
                    <img class="img-fluid w-100 h-100" src={image_src} style="object-fit: cover;">
                    <div class="overlay">
                        <div class="mb-2">
                            <a class="badge badge-danger text-uppercase font-weight-semi-bold p-2 mr-2"
                                href="">{subject}</a>
                            <a class="text-white" href=""><small>{date}</small></a>
                        </div>
                        <a class="h6 m-0 text-white text-uppercase font-weight-semi-bold" href={href}>{title}</a>
                    </div>
                </div>
            </div>
        """

    for item in feed.entries[5:]:
        title = item.title
        length = len(item.title)
        source_url = item.link
        description = item.description[length+1:]
        content = item.content[0]['value']
        image_src = item.links[0]['href']
        date = item.published
        href = f"single.html?title={quote(title)}&description={quote(description)}&image_src={quote(image_src)}&source_url={quote(source_url)}&date={quote(date)}&subject={quote(subject)}&content={quote(content)}"
        remaining_html_content += f"""
        <div class="position-relative overflow-hidden" style="height: 300px;">
            <img class="img-fluid h-100" src="{image_src}" style="object-fit: cover;">
            <div class="overlay">
                <div class="mb-2">
                    <a class="badge badge-danger text-uppercase font-weight-semi-bold p-2 mr-2" href="">{subject}</a>
                    <a class="text-white" href=""><small>{date}</small></a>
                </div>
                <a class="h6 m-0 text-white text-uppercase font-weight-semi-bold" href="{href}">{title}</a>
            </div>
        </div>
        """

    return main_html_content, secondary_html_content, remaining_html_content

def get_search_results(keyword):
    keyword_low = keyword.lower()
    feed = fetch_news()
    html_content = ""
    for item in feed.entries:
        if keyword_low in item.title.lower():
            title = item.title
            length = len(item.title)
            subject = 'Ekonomi'
            source_url = item.link
            description = item.description[length+1:]
            content = item.content[0]['value']
            image_src = item.links[0]['href']
            date = item.published
            href = f"single.html?title={quote(title)}&description={quote(description)}&image_src={quote(image_src)}&source_url={quote(source_url)}&date={quote(date)}&subject={quote(subject)}&content={quote(content)}"
            html_content += f"""
            <div class="col-lg-6">
                <div class="position-relative mb-3">
                    <img class="img-fluid w-100" src="{image_src}" style="object-fit: cover;">
                    <div class="bg-white border border-top-0 p-4">
                        <div class="mb-2">
                            <a class="badge badge-danger text-uppercase font-weight-semi-bold p-2 mr-2"
                                href={href}>{subject}</a>
                            <a class="text-body" href=""><small>{date}</small></a>
                        </div>
                        <a class="h4 d-block mb-3 text-secondary text-uppercase font-weight-bold" href="">{title}</a>
                        <p class="m-0">{description}</p>
                    </div>
                    <div class="d-flex justify-content-between bg-white border border-top-0 p-4">
                    </div>
                </div>
            </div>
            """

    return html_content
