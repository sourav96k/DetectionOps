import json
from datetime import date


with open("data/topics.json") as f:
    data=json.load(f)


topic=data["categories"][0]


article=f"""

# {topic}


## Introduction

Latest cybersecurity research and analysis.


## Overview

This article explains {topic} concepts,
tools, attacks and mitigation.


## Detection

Security teams should monitor:

- Logs
- Alerts
- Indicators
- User activity


## Mitigation

Recommended security practices:

- Update systems
- Monitor events
- Apply security controls


## Conclusion

Continuous learning improves cybersecurity defense.

"""


filename=f"drafts/{topic.replace(' ','-')}.md"


with open(filename,"w") as f:
    f.write(article)


print("Draft created:",filename)
