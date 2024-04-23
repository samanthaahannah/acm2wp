# acm2wp
Python script to process digital library website open articles into ACM Games: Research and Practice website word press format, including reference/anchors conversion

[![Twitter Follow](https://img.shields.io/twitter/follow/GamesACM.svg?style=social&label=Follow)](https://twitter.com/GamesACM)
[![Youtube Subscribe](https://img.shields.io/youtube/channel/subscribers/UCfdm-h_KkO1GumtqLUGWfFw?style=social)](https://www.youtube.com/channel/UCfdm-h_KkO1GumtqLUGWfFw?sub_confirmation=1)
[![Github Stars](https://img.shields.io/github/stars/farpeek/acm2wp?style=social)](https://github.com/farpeek/acm2wp/stargazers)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg)](https://github.com/farpeek/acm2wp/graphs/commit-activity)
[![Open in Visual Studio Code](https://img.shields.io/badge/-Open%20in%20VSCode-007acc?logo=Visual+Studio+Code&logoColor=FFFFFF)](https://vscode.dev/github/farpeek/acm2wp)

# Usage

python acm2wp [input.html] [output.html] [replacements.txt]

# VC Code Example Workflow

Install Visual Studio Code [![VSCode Download](https://img.shields.io/badge/-VSCode%20Download-007acc?logo=Visual+Studio+Code&logoColor=FFFFFF)](https://code.visualstudio.com/download)

Within VSCode install the python extension [![Python extension](https://img.shields.io/badge/-Python%20Extension-007acc?logo=Python+Extension&logoColor=FFFFFF)](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

Open the local folder where you have cloned or downloaded this github project from within VSCode

Open this project's acm2wp.py file in VSCode

Select and copy only the text with references of any open article from the digital library and place into an [input.html] file in the project folder.

Click Run+Debug in VSCode (SHIFT+CMD+D on Mac)

Add command-line arguments for the files, "input.html output.html replacements.txt" and return will run the script

You may also install the HTML Preview extension to preview intput and output html files as they would in a browser, and check for conversions of reference links and headings, any corrections of digital library formatting, etc.

The resulting output.html file's contents will have the format suitable for pasting into the text field of a wordpress post.
That is, in wordpress editor's post content field, select 'text' as opposed to 'visual' and paste in the output.html file's content.

Save draft and preview. The result should be similar to that seen in VSCode html preview window.


# Notes

Different articles have different headings and issues, so replacements.txt might sensibly update according to these as encountered.

# Todo

Automate copyright transfer per article
Convert to wordpress plugin
Auto scrape all open articles in a journal issue


