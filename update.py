
import os
import datetime
import xml.etree.ElementTree as ET

class Sitemap:
    html_documents = []

    def get_filename_without_extension(self, path):
        """Extracts the filename without extension from a given path."""
        filename = os.path.basename(path)
        filename_without_extension = os.path.splitext(filename)[0]
        filename_without_extension = filename_without_extension.replace('.component', '')
        return filename_without_extension 
    
    def scan_directory(self, path, sitemap):
        if os.path.isdir(path):
            for dir in os.listdir(path):
                self.scan_directory(os.path.join(path, dir), sitemap)
        else:
            if (path.endswith('.html')):
                file_name = self.get_filename_without_extension(path)
                self.html_documents.append(file_name)
                
    def generate(self):
        SCAN_PATH = 'C:\\src\\nehsanet-app\\nehsanet\\src\\app'
        SITEMAP_FILENAME = 'sitemap.xml'
        IGNORE_FOLDERS = ["shared-components", "flashcards"]


        if os.path.exists(SITEMAP_FILENAME):
            os.remove(SITEMAP_FILENAME)
            
        with open(SITEMAP_FILENAME, 'w') as file:
            file.write("<?xml version='1.0' encoding='UTF-8'?>\n")
            file.write("<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>\n")
            self.scan_directory(SCAN_PATH, sitemap)            
            for html_document in self.html_documents:
                if html_document in IGNORE_FOLDERS:
                    continue
                file.write(f"<url><loc>https://www.nehsa.net/#/{html_document}</loc><lastmod>f{datetime.date.today().strftime('%Y-%m-%d')}</lastmod><changefreq>daily</changefreq><priority>1</priority></url>\n")
            file.write("</urlset>")
        
        with open(SITEMAP_FILENAME, 'r') as file:
            print(file.read())
            
        print(f"Sitemap generated successfully: {len(self.html_documents)} pages found.")
            
if __name__ == '__main__':
    sitemap = Sitemap()
    sitemap.generate()