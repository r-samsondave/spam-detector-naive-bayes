from src.data_loader import load_dataset
from src.data_split import split_data
from src.vocabulary import build_vocabulary
from src.naive_bayes import *
documents, labels = load_dataset()

# split the dataset into training and testing sets.
x_train, y_train, x_test, y_test = split_data(documents, labels)

# vocabulary using training data
vocabulary = build_vocabulary(x_train)
vocabulary_size = len(vocabulary)

# Identifier of count_words
(spam_word_counts,
 total_spam_count,
 not_spam_word_counts,
 total_not_spam_count) = count_words_by_class(x_train, y_train)

# class_prior for spam and not_spam
prior_spam = calculate_class_prior("spam", y_train)
prior_not_spam = calculate_class_prior("not_spam", y_train)


print(calculate_class_log_score("hey bro pull up, lets smoke",
                                prior_not_spam,
                                not_spam_word_counts,
                                total_not_spam_count,
                                vocabulary,
                                vocabulary_size))

print(calculate_class_log_score("hey bro pull up, lets smoke",
                                prior_spam,
                                spam_word_counts,
                                total_spam_count,
                                vocabulary,
                                vocabulary_size))