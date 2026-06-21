import os
import glob
import shutil


drafts = "drafts/"
articles = "articles/"


os.makedirs(articles, exist_ok=True)


for file in glob.glob(drafts + "*.md"):

    name = os.path.basename(file).replace(".md","")

    with open(file, "r") as f:
        content = f.read()


    html = f"""
<!DOCTYPE html>

<html>

<head>

<title>{name}</title>

<link rel="stylesheet" href="../style.css">

</head>


<body>


<header class="navbar">

<div class="logo">
DetectionOps
</div>


<a href="../index.html">
Home
</a>


</header>


<main class="article-page">


<pre>

{content}

</pre>


</main>


</body>

</html>
"""


    output = f"{articles}{name}.html"


    with open(output,"w") as f:
        f.write(html)


    print("Published:", output)
