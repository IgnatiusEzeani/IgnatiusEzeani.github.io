---
permalink: /
title: "Dr Ignatius Ezeani"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
Hello and thanks for stopping by. I am Ignatius, a computer scientist, an AI and NLP researcher and a [Senior Teaching and Research Associate](https://www.lancaster.ac.uk/scc/about-us/people/ignatius-ezeani) with the [School of Computing and Communications](https://www.lancaster.ac.uk/scc/) at [Lancaster University, UK](https://www.lancaster.ac.uk/) as well as a visiting Senior Lecturer at [Nnamdi Azikiwe University, Nigeria](https://www.unizik.edu.ng/).

I have a Bachelor (1st) in Computer Science, a Masters in Advanced Software Engineering, and a PhD in Natural Language Processing (NLP). I am interested in the application of NLP techniques in building resources for low-resource languages especially African languages, but my interests span other related areas like <em>corpus linguistics</em>, <em>distributional semantics</em>, <em>information retrieval and extraction</em>, <em>machine learning</em>, <em>data science</em>, <em>deep neural models</em> and general AI.

My current research work focuses on the efficient adaption of existing natural language processing tools and techniques to dealing with the challenges of integrating majority of the low-resource languages in a globalized world for task-oriented systems. I have contributed in building tools that support languages like Igbo and Welsh and I am currently working on other low-resource languages. You can reach me via any of the platforms shown here for a quick chat. Alternatively, you can check out the other pages on this site for my works and creative outputs.

Currently, I am the lead software developer on the [£814k SBE-UKRI](https://gtr.ukri.org/person/3174DF16-E0EE-44F2-B458-C6535A43016B) project trying to understand imprecise space and time in textual narratives through qualitative representations, reasoning, and visualization. Before that, I recently worked on the ongoing [£80k FreeTxt](https://gtr.ukri.org/projects?ref=AH%2FW004844%2F1) project and completed the £90k Cardiff-Lancaster collaboration [Welsh Text Creator](https://ucrel-welsh-summarizer-appapp-b2vcdc.streamlit.app/) project. I led the creation of the [Igbo-English MT benchmark dataset](https://www.research.lancs.ac.uk/portal/en/datasets/igboenglish-machine-translation-an-evaluation-benchmark(b2d87fb1-c9d2-4840-8de4-f52d4e2045da).html), a $23k Facebook-funded project. I am part of [Masakhane Initiative](https://www.masakhane.io/), the most vibrant AfricanNLP research community where I am also leading a Google-backed Question Answering dataset creation project for Igbo. For the 2nd year, I am on the [Technical Advisory Panel of the Lacuna Fund](https://lacunafund.org/language-technical-advisory-panel/) granting over $1m in 2021 to fund the creation of African language datasets.

<!-- A data-driven personal website
======
You keep these various markdown (.md), YAML (.yml), HTML, and CSS files in a public GitHub repository. Each time you commit and push an update to the repository, the [GitHub pages](https://pages.github.com/) service creates static HTML pages based on these files, which are hosted on GitHub's servers free of charge.

Many of the features of dynamic content management systems (like Wordpress) can be achieved in this fashion, using a fraction of the computational resources and with far less vulnerability to hacking and DDoSing. You can also modify the theme to your heart's content without touching the content of your site. If you get to a point where you've broken something in Jekyll/HTML/CSS beyond repair, your markdown files describing your talks, publications, etc. are safe. You can rollback the changes or even delete the repository and start over -- just be sure to save the markdown files! Finally, you can also write scripts that process the structured data on the site, such as [this one](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb) that analyzes metadata in pages about talks to display [a map of every location you've given a talk](https://academicpages.github.io/talkmap.html). 

Getting started
======
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section

Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

Create content & metadata
------
For site content, there is one markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

I have also created [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the academicpages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring academicpages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful. -->
