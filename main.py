import tika
from tika import parser
from tika import config

def print_current_setup():
  # Returns a LOT of metadata
  print(config.getDetectors())
  print(config.getMimeTypes())
  print(config.getParsers())


if __name__ == "__main__":
  pdf1 = parser.from_file('./pdfs/example.pdf')

  print("METADATA:", pdf1["metadata"]) # -> A medium-sized pararagraph
  print("STATUS:", pdf1["status"]) # HTTP Req stauts

  print("KEYS:", pdf1.keys()) # ->[status, metadata, content]
  # print("VALUES", pdf1.values()) # 3rd value repr. PDF's string
  
  # Content is a string. Damn... Gotta use RegEx
  print("CONTENT LENGTH", len(pdf1["content"]), "characters")
  print("CONTENT:", pdf1["content"][:1000])

  
