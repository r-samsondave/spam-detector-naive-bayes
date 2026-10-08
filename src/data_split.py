import random # for data shuffling



def split_data(documents, labels):
    x_train = []
    y_train = []
    x_test = []
    y_test = []

    # zipping and shuffling dataset
    dataset = list(zip(documents, labels))
    random.shuffle(dataset)

    # calculation of train size
    total = len(dataset)
    train_size = int(total * 0.8) # 80% of dataset

    # splitting dataset 80/20
    training_set = dataset[:train_size]
    testing_set = dataset[train_size:]

    for document, label in training_set:
        x_train.append(document)
        y_train.append(label)

    for document, label in testing_set:
        x_test.append(document)
        y_test.append(label)


    return x_train, y_train, x_test, y_test



print(split_data(documents, labels))


