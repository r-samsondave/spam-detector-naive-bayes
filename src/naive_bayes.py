from preprocessing import preprocessing

def count_words_by_class(x_train, y_train):

    # dictionary for spam and not_spam
    spam_word_counts = {}
    not_spam_word_counts = {}

    # total words in each class
    total_spam_words = 0
    total_not_spam_words = 0

    for document, label in zip(x_train, y_train):
        tokens = preprocessing(document)

        # check if it's spam or not_spam
        if label == "spam":
            for word in tokens:
                total_spam_words += 1

                if word in spam_word_counts:
                    spam_word_counts[word] += 1
                else:
                    spam_word_counts[word] = 1

        else:
            for word in tokens:
                total_not_spam_words += 1

                if word in not_spam_word_counts:
                    not_spam_word_counts[word] += 1
                else:
                    not_spam_word_counts[word] = 1


    return spam_word_counts, total_spam_words, not_spam_word_counts, total_not_spam_words