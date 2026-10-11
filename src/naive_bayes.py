from src.preprocessing import preprocessing
import math

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

        elif label == "not_spam":
            for word in tokens:
                total_not_spam_words += 1

                if word in not_spam_word_counts:
                    not_spam_word_counts[word] += 1
                else:
                    not_spam_word_counts[word] = 1

        else:
            raise ValueError(f'Unknown label: {label}')


    return spam_word_counts, total_spam_words, not_spam_word_counts, total_not_spam_words


def calculate_likelihood(word,
                         class_word_counts,
                         total_class_word,
                         vocabulary_size):

    word_count = class_word_counts.get(word, 0)
    smoothed_word_count = word_count + 1
    smoothed_total_word_count = total_class_word + vocabulary_size

    likelihood = smoothed_word_count / smoothed_total_word_count

    return likelihood


def calculate_class_prior(class_name, y_train):
    class_count = y_train.count(class_name) # count specific class
    training_set_size = len(y_train) # overall size of class

    class_prior = class_count/training_set_size


    return class_prior

def calculate_class_log_score(message,
                        class_prior,
                        class_word_counts,
                        total_class_words,
                        vocabulary,
                        vocabulary_size):

    tokens = preprocessing(message)
    score = math.log(class_prior)

    for word in tokens:
        if word in vocabulary:
            word_likelihood = calculate_likelihood(word,
                                     class_word_counts,
                                     total_class_words,
                                     vocabulary_size)

            score += math.log(word_likelihood)


    return score
