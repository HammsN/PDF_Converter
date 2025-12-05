from  playwright.sync_api import sync_playwright
from pathlib import Path
import sys

#terminal app to get file (microsoft word, .txt wgatever), paste into website converter using selenium/beautifulsoup, paste next to file location

#Doc1.docx

def get_file_name() -> str:
    if len(sys.argv) > 1:
        FILE = Path(sys.argv[1])
        if FILE.exists():
            return FILE
    else:
        FILE = Path(input("Name of file to convert: "))
        if FILE.exists():
            return FILE


WORD_TO_PDF = "https://www.ilovepdf.com/word_to_pdf" 
FILE = get_file_name()

if FILE:
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch()
        page = browser.new_page()
        page.goto(WORD_TO_PDF)
        
        page.locator('input[type="file"]').set_input_files(FILE)
        
        page.click('#processTask')
        
        with page.expect_download() as download_info:
            page.click('.downloader__btn')
            print(f"Download info: {download_info}")
        download = download_info.value
        
        download.save_as(f"{download.suggested_filename}")
            
        print("Done")
else:
    print("Invalid file. (Missing/mispelled?)")