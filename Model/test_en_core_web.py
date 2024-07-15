import spacy
# import os

# Get the directory of the installed SpaCy package
# spacy_dir = os.path.dirname(spacy.__file__)
# print(spacy_dir)

nlp = spacy.load("en_core_web_md")

# #Assuming the Entity Linker needs to be added manually
# if "entity_linker" not in nlp.pipe_names:
#     nlp.add_pipe("entity_linker", last=True)

# Process text
doc = nlp("This is a sentence mentioning Apple.")
for ent in doc.ents:
    print(ent.text, ent.label_, ent.kb_id_)

# import spacy

# # Replace this with the actual path to your model directory
# model_path = 'C:\Users\nisha\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\spacy'
# nlp = spacy.load(model_path)
