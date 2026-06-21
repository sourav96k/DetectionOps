import json
import os
from datetime import date


with open("data/topics.json") as f:
    data = json.load(f)


topics = data["categories"][:3]


os.makedirs("drafts", exist_ok=True)


for topic in topics:

    article = f"""
# {topic}

## Introduction

Daily cybersecurity analysis about {topic}.

Date: {date.today()}


## Overview

This article explains:

- Current trends
- Security risks
- Detection methods
- Mitigation techniques


## Detection

Security teams should monitor:

- Logs
- Alerts
- Network activity
- Endpoint events


## Mitigation

Recommended actions:

- Patch systems
- Improve monitoring
- Update security controls


## Conclusion

Continuous cybersecurity research helps defenders.

"""


    filename = f"drafts/{topic.replace(' ','-')}.md"


    with open(filename,"w") as f:
        f.write(article)


    print("Created:", filename)
