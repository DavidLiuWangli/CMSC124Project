from tokens import KEYWORDS
import re

pattern = re.compile(r'^BTW\s.*$')
print(pattern.match("BTW hello my dear"))  # Should match "I HAS A"

