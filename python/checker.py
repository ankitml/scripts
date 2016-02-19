import numpy

def edit_distance(correct_ans, student_ans):
    """
    :param correct_ans: correct answer, can be multiple words
    :param student_ans: answer submitted by student, can be multiple words
    :return  The Edit Distance between 2 strings
    """

    len_correct_ans = len(correct_ans)
    len_student_ans = len(student_ans)

    answers = numpy.zeros((len_correct_ans+1,len_student_ans+1))

    for j in range(0,len_correct_ans+1):
        answers[j][0]=j

    for i in range(0, len_student_ans+1):
        answers[0][i]=i


    for i in range(len_correct_ans):
        for j in range(len_student_ans):
            if(correct_ans[i]==student_ans[j]):
                answers[i+1][j+1]=answers[i][j]
            elif(correct_ans[i]!=student_ans[j]):
                answers[i+1][j+1]=1+min(answers[i+1][j],min(answers[i][j+1], answers[i][j]))
    return answers[len_correct_ans][len_student_ans]


def answer_checker(correct_ans,student_input):
    """
    :param correct_ans,param student_input:
    :what it does: 1. Changes all input upper-case strings to lower-case strings
                   2. Checks edit distance between correct answer and student answer
                   3. Takes maximum acceptable edit distance as 2
    :return: Checks the answer and prints appropriate result(correct, wrong).
    """
    lower_case_student_input=student_input.lower()
    student_input_set=lower_case_student_input.split(' ')
    lower_case_correct_ans=correct_ans.lower()
    correct_answer_set=lower_case_correct_ans.split(' ')

    elements=[]
    num_words=len(correct_answer_set)                               #considering length of both answers is same

    for i in range(0,num_words):
        elements.append(edit_distance(student_input_set[i],correct_answer_set[i]))

    max_distance_in_all_words=max(elements)
    import ipdb; ipdb.set_trace() 
    if max_distance_in_all_words>4:
        print "Wrong"
    else:
        print "Correct"


