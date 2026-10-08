import re # For text processing

def preprocessing(document):
    lowercased_document = document.lower()
    cleaned_document = re.sub(r"[^a-zA-Z0-9\s]", " ", lowercased_document)
    tokenized_text = cleaned_document.split()

    return tokenized_text