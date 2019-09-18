from docx import Document
from scriptCleaner import cleanScript
from os.path import splitext

filePath = "./scripts/english/Putin's_Forgotten_Children-Transcript45'.txt"
file_name, extension = splitext(filePath)
print(file_name)


if extension == ('.txt' or '.docx'):
    doc = Document(filePath)
    paragraphs = doc.paragraphs

    for p in paragraphs:
        if not p.text.strip():
            continue
        else:
            script = cleanScript(p.text)
            if script:
                f = open('output/' + 'output' + '.txt', 'a')
                f.write(script.encode("utf8") + '\n')
                f.close()
else:
    print("Scripts needs to be a docx or a txt file")
