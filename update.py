import json
import os
import datetime
import xml.etree.ElementTree as ET
from settings import Settings
from sitemap import SitemapItem


class Sitemap:
    html_documents: SitemapItem = []
    settings = Settings()
 

    def get_filename_without_extension(self, path):
        """Extracts the filename without extension from a given path."""
        filename = os.path.basename(path)
        filename_without_extension = os.path.splitext(filename)[0]
        filename_without_extension = filename_without_extension.replace(
            ".component", ""
        )
        return filename_without_extension

    def scan_directory(self, path, sitemap):
        print(f"Scanning directory or file: {path}")

        for root, _, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                if os.path.isdir(file):
                    pass
                else:
                    if full_path.endswith(".html"):
                        file_name = self.get_filename_without_extension(full_path)
                        item: SitemapItem = SitemapItem()                        
                        for mapping in self.settings.mappings:
                            if mapping["folder"] == file_name:
                                item.loc = mapping["url_path"]
                                break
                            else:
                                item.loc = file_name
                        item.lastmod = os.path.getmtime(full_path)
                        item.changefreq = SitemapItem.Frequency.DAILY
                        for override in self.settings.priority_overrides:
                            #print(override["page"], item.loc)
                            if item.loc in override["folder"]:
                                item.priority = override["priority"]
                                break
                            else:
                                item.priority = 0.5
                        item.full_path = full_path
                        self.html_documents.append(item)
    
    def load_settings(self, file_path):
        print(f"Loading settings from file: {file_path}")
        with open(file_path, 'r') as file:
            data = json.load(file)
        return Settings(**data)

    def generate(self):
        SITEMAP_FILENAME = "sitemap.xml"
        self.settings = self.load_settings("settings.json")

        if os.path.exists(SITEMAP_FILENAME):
            os.remove(SITEMAP_FILENAME)

        with open(SITEMAP_FILENAME, "w") as file:
            file.write("<?xml version='1.0' encoding='UTF-8'?>\n")
            file.write("<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>\n")
            self.scan_directory(self.settings.search_path, sitemap)
            if self.settings.use_hash:
                self.settings.base_url += "/#"
            for html_document in self.html_documents:
                if any(item in html_document.full_path for item in self.settings.ignore_folders):
                    # print("Skipping ignored folder: ", html_document.full_path)
                    continue

                url = f"{self.settings.base_url}/{html_document.loc}"

                if not url.endswith('/'):
                    url += '/'

                modified_date = datetime.datetime.fromtimestamp(
                    html_document.lastmod
                ).strftime("%Y-%m-%d")
                file.write(
                    f"<url><loc>{url}</loc><lastmod>{modified_date}</lastmod><changefreq>{html_document.changefreq.value}</changefreq><priority>{html_document.priority}</priority></url>\n"
                )
            file.write("</urlset>")

        with open(SITEMAP_FILENAME, "r") as file:
            print(file.read())

        print(
            f"Sitemap generated successfully: {len(self.html_documents)} pages found."
        )


if __name__ == "__main__":
    sitemap = Sitemap()
    sitemap.generate()
