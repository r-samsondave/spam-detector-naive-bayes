def load_dataset():
    documents = []
    labels = []
    with open("data/raw/sms+spam+collection/SMSSpamCollection", "r") as file:

        for line in file:
            line = line.strip()
            label, message = line.split("\t", 1)

            if label == "ham":
                label = "not_spam"

            documents.append(message)
            labels.append(label)

    return documents, labels

