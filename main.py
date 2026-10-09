from src.data_loader import load_dataset
from src.data_split import split_data
from src.vocabulary import build_vocabulary

documents, labels = load_dataset()

# split the dataset into training and testing sets.
x_train, y_train, x_test, y_test = split_data(documents, labels)

vocabulary = build_vocabulary(x_train)

print("Vocabulary size:", len(vocabulary))
print("First 10 words:", vocabulary[:10])