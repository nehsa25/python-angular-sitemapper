# python-angular-sitemapper
Generates a sitemap.xml file based on the file structure of an Angular website.

# Usage:
c:\python .\update.py

# Settings:
```json
{
    "base_url": "The protocol/domain portion of the url",
    "priority_overrides": [
        {
            "folder": "A specific page",
            "priority": "The priority as a float (0.0 - 1.0)"
        }
    ],
    "ignore_folders": [
        "Pages within these directories will not be in the sitemap.xml",
    ],
    "mappings": [
        {
            "folder": "The folder as it's shown in the filesystem",
            "url_path": "The path after the domain as it's represented in the routes file"
        }
    ]
}

```