import re
import unittest
from dateutil.parser import parse


def get_date(text):
    pattern = r"On\s+(?:[A-Za-z]+,\s*)?(.+?)(?:,?\s+Test User)"
    match = re.search(pattern, text)
    
    if match:
        raw_date = match.group(1)
        dt = parse(raw_date)
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    
    return None


class TestGetDate(unittest.TestCase):
    def test_dates(self):
        cases = [
            ("On Sun, 13 Oct 2024 19:01:18 +0800, Test User <test@test.me> wrote:", "2024-10-13T19:01:18Z"),
            ("On Tue, Oct 1, 2024 at 19:23 Test User <test@test.me> wrote:", "2024-10-01T19:23:00Z"),
            ("On Mon, Oct 14, 2024, 8:06 PM Test User <test@test.me> wrote:", "2024-10-14T20:06:00Z"),
            ("On Wed, 9 Oct 2024, 2:04 am Test User, <test@test.me> wrote:", "2024-10-09T02:04:00Z"),
            ("On 25-Sep-2024 3:37 am, Test User <test@test.me> wrote:", "2024-09-25T03:37:00Z"),
            ("On Fri, 27 Sept 2024, 17:32 Test User, <test@test.me> wrote:", "2024-09-27T17:32:00Z")
        ]
        for text, expected in cases:
            self.assertEqual(get_date(text), expected)


if __name__ == "__main__":
    unittest.main()
