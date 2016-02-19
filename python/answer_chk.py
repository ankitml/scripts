import numpy

TOL_ERROR = 1
SPECIAL_CHARS = [';', ',', '.', '/', '[', ']', '\'']
EASY_ERRORS = {
    'a': ['q', 'w', 's', 'z'],
    'b': ['v', 'g', 'h', 'n'],
    'c': ['x', 'd', 'f', 'v'],
    'd': ['s', 'e', 'r', 'f', 'c', 'x'],
    'e': ['w', 's', 'd', 'r'],
    'f': ['r', 't', 'g', 'v', 'c', 'd'],
    'g': ['t', 'y', 'h', 'b', 'v', 'f'],
    'h': ['y', 'u', 'j', 'n', 'b', 'g'],
    'i': ['u', 'j', 'k', 'o', '9', '8'],
    'j': ['u', 'i', 'k', 'm', 'n', 'h'],
    'k': ['i', 'o', 'l', ',', 'm', 'j'],
    'l': ['o', 'p', ';', '.', ',', 'k'],
    'm': ['n', 'j', 'k', ','],
    'n': ['b', 'h', 'j', 'm'],
    'o': ['i', 'k', 'l', 'p', '0', '9'],
    'p': ['0', '-', '[', ';', 'l', 'o'],
    'q': ['1', '2', 'w', 'a'],
    'r': ['4', '5', 't', 'f', 'd', 'e'],
    's': ['w', 'e', 'd', 'x', 'z', 'a'],
    't': ['5', '6', 'y', 'g', 'f', 'r'],
    'u': ['7', '8', 'i', 'j', 'h', 'y'],
    'v': ['f', 'g', 'b', 'c'],
    'w': ['2', '3', 'e', 's', 'a', 'q'],
    'x': ['z', 's', 'd', 'c'],
    'y': ['t', 'g', 'h', 'u', '7', '6'],
    'z': ['a', 's', 'x'],
    '1': [],
    '2': [],
    '3': [],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
    '8': [],
    '9': [],
    '0': [],
}


def normalize_text(text):

    """
    :rtype: list of strings
    :param text: input text to be normalized
    :return: returns lower-case and removes special characters from the input string
             and returns set of words from the string

    examples (input : Narendra Modi is India's PM.
              output :[ ''narendra', 'modi', 'is', 'indias', 'pm']
              )
    """

    text = text.lower()
    for char in text:
        if char in SPECIAL_CHARS:
            text = text.replace(char, '')
    return text.split(' ')


def edit_distance(correct_ans, student_ans):

    """
    :rtype: int
    :param correct_ans: correct answer, can be multiple words
    :param student_ans: answer submitted by student, can be multiple words
    :return  The Edit Distance between 2 strings
    """

    no_characters_correct_ans = len(correct_ans)
    no_characters_student_ans = len(student_ans)

    answers = numpy.zeros((no_characters_correct_ans+1, no_characters_student_ans+1))
    for i in range(0, no_characters_correct_ans+1):
        for j in range(0, no_characters_student_ans+1):
            answers[i][j] = 0

    # If first string is empty, only option is to
    # insert all characters of second string
    for j in range(0, no_characters_correct_ans + 1):
        answers[j][0] = j

    # If second string is empty, only option is to
    # remove all characters of second string
    for i in range(0, no_characters_student_ans + 1):
        answers[0][i] = i

    for i in range(no_characters_correct_ans):
        for j in range(no_characters_student_ans):
            # If last characters are same, ignore last char
            # and recur for remaining string
            if correct_ans[i] == student_ans[j]:
                answers[i + 1][j + 1] = answers[i][j]
            # If last character are different, consider all
            # possibilities and find minimum
            elif correct_ans[i] != student_ans[j]:
                # If characters are easy errors of each other
                # add only 0.3 instead of 1
                if student_ans[j] in EASY_ERRORS[correct_ans[i]]:
                    answers[i+1][j+1] = min(
                            answers[i + 1][j],       # insert
                            min(answers[i][j + 1],   # remove
                                answers[i][j]))+0.3  # replace
                else:
                    answers[i + 1][j + 1] = 1 + min(
                            answers[i + 1][j],       # insert
                            min(answers[i][j + 1],   # remove
                                answers[i][j]))      # replace

    return answers[no_characters_correct_ans][no_characters_student_ans]


def word_exists(key_word, student_ans):
    """
    :rtype: boolean
    :param key_word: Keyword to be searched in student's answer
    :param student_ans: List of words in student's answer
    :return: whether the keyword exists in students's answer or not
    """
    for word in student_ans:
        if edit_distance(word, key_word) <= TOL_ERROR:
            return True
    return False


def answer_check(correct_ans, student_ans):
    """
    :rtype: None
    :param correct_ans: Correct answer
    :param student_ans: Students's answer
    :return: prints whether student answer is wrong or right
    """

    elements = []
    for word in correct_ans:
        elements.append(word_exists(word, student_ans))
    exists = all(elements)
    if exists:
        print "Correct Answer"
    else:
        print "Wrong Answer"

#student = raw_input('> Enter student answer:' )
#correct = raw_input('> Enter Correct answer: ')

#student_input = normalize_text(student)
#correct_input = normalize_text(correct)

#answer_check(correct_input, student_input)
