from tika import parser
import re

def print_lines(lines=15, chars=60, sep="-"):
  """Prints in console n lines composed of m repetitions of a given character.
   Useful for formatting and separation"""
  for i in range(lines):
    print(sep * chars)


def process_section(text, i, save_obj=None):
  """Process the text section. For now, prints it in console
  Future behavior will be storing the section string in a dict"""
  print(f"SECTION {i}:")
  print(text)
  print_lines()


def look_for_sections(text):
  """Find and separate the sections from the text.
  Then it process those sections using process_section()"""

  # List of known sections to look for
  sections = ['EJECUTIVO MERCANTIL', 'EXTRAORDINARIO CIVIL',
    'HIPOTECARIO', 'JURISDICCION VOLUNTARIA', 'ORDINARIO CIVIL']
  
  print("RESULTS OF SECTION SEARCH")
  # Look for "section A-section B" patterns
  s = 1
  len_sections = len(sections)
  a = 0
  while a < len_sections:
    # Confirm section A exists so A-B search pattern can begin
    if f"\n\n{sections[a]}" in text:
      b = a + 1
      while b < len_sections:
        # Confirm section B exists so we can extract that A-B section
        if f"\n\n{sections[b]}" in text:
          # Build search pattern. Example: "\n\nHIPOTECARIO.*\n\nORDINARIO CIVIL"
          p = f"\n\n{sections[a]}.*\n\n{sections[b]}"
          # Look for pattern and process it
          # TODO: PatternNotFound error handling
          res = re.findall(p, text, re.S)
          process_section(res[0], s)
          # B is the next section to start looking
          a = b
          s += 1
          break
        # Keep looking for possible sections B
        else:
          b += 1
      # If there wasn't any section B, section A takes the remaining text
      if b == len_sections:
        # Find and process the section.
        res = re.findall(f"\n\n{sections[a]}.*", text, re.S)
        process_section(res[0], s)
        # Break loop. There are no more sections to look.
        break
    # Else, search for next possible section A
    else:
      a += 1


def look_for_useful_metadata(metadata_str):
  # Useful keys: Author, Creation-Date, dc:language, resourceName
  keys = ['Author', 'Creation-Data', 'dc:language', 'resourceName']
  pass



if __name__ == "__main__":
  # Take text from the pdf as a string
  pdf1 = parser.from_file('./pdfs/example.pdf')

  look_for_sections(pdf1["content"])

