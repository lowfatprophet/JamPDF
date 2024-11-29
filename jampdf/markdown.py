from typing import Any

import frontmatter
import markdown


def parse_input(file: str) -> tuple[dict[str, Any], str]:
    metadata, content = frontmatter.parse(file)
    content = markdown.markdown(content)
    return (metadata, content)
