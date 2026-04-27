import html
import re
import sys
import urllib.parse
import urllib.request


def get_page_title(url):
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }
        req = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req, timeout=7) as response:
            page = response.read().decode("utf-8", errors="replace")
            title_search = re.search(r"<title>(.*?)</title>", page, re.IGNORECASE | re.DOTALL)
            if title_search:
                title = title_search.group(1).strip()
                title = html.unescape(title)
                return title.replace("\n", " ").replace("\r", "")
    except Exception:
        pass
    return url.split("/")[-1] or "Article"


def get_short_url(long_url):
    headers = {"User-Agent": "Mozilla/5.0"}
    api_url = f"https://is.gd/create.php?format=simple&url={urllib.parse.quote(long_url)}"

    try:
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req) as response:
            return response.read().decode("utf-8").strip()
    except Exception as e:
        return f"ShortenerError: {e}"


def main():
    if len(sys.argv) < 2:
        print("Usage: lorg [Original_URL] [Optional_Title]")
        return

    input_url = sys.argv[1]

    if len(sys.argv) > 2:
        title = sys.argv[2]
    else:
        print(f"[*] Fetching title from {input_url}...")
        title = get_page_title(input_url)

    short_url = get_short_url(input_url)

    org_format = f"[[{short_url}][{title}]]"

    print("\n" + "=" * 30)
    print(org_format)
    print("=" * 30 + "\n")


if __name__ == "__main__":
    main()
