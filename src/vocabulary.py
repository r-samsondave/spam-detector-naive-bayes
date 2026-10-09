from src.preprocessing import preprocessing

def build_vocabulary(documents):
    vocabulary = set()

    for document in documents:
        preprocessed_document = preprocessing(document)
        vocabulary.update(preprocessed_document)

    return sorted(vocabulary)