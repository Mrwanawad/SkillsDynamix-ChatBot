from docling.document_converter import DocumentConverter
from tqdm import tqdm

def scrap_data_from_website( website_link: str ) :
    
    convertor = DocumentConverter()
    
    result = convertor.convert( website_link )
    document = result.document
    
    return document.export_to_markdown() 


if __name__ == '__main__' :
    print( scrap_data_from_website( 'https://www.sutherlandglobal.com/about-us' ) )