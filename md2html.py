import markdown


def parse_markdown_to_html(filename):
    """
    :param filename: Filename of markdown note (Without suffix .md).
    :return: The html code corresponding to the markdown note
    """
    with open(f'./static/md/{filename}.md', 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    f.close()

    # Convert Markdown into HTML
    html = markdown.markdown(markdown_text)

    return html
