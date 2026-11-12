import re
from dateutil.parser import parse


def get_date(text):
    pattern = r"On\s+(?:[A-Za-z]+,\s*)?(.+?)(?:,?\s+Test User)"
    match = re.search(pattern, text)

    if match:
        raw_date = match.group(1)
        dt = parse(raw_date)
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    return None


test_strings = [
    "On Sun, 13 Oct 2024 19:01:18 +0800, Test User <test@test.me> wrote:",
    "On Tue, Oct 1, 2024 at 19:23 Test User <test@test.me> wrote:",
    "On Mon, Oct 14, 2024, 8:06 PM Test User <test@test.me> wrote:",
    "On Wed, 9 Oct 2024, 2:04 am Test User, <test@test.me> wrote:",
    "On 25-Sep-2024 3:37 am, Test User <test@test.me> wrote:",
    "On Fri, 27 Sept 2024, 17:32 Test User, <test@test.me> wrote:"
]

for line in test_strings:
    result = get_date(line)
    print(result)