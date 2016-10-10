"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The benefits of object orientation include

   a. Abstraction

        Details (regarding data and/or behavior) can be concealed.

   b. Encapsulation

        Data and/or behavior can be organized and kept together.
   
   c. Polymorphism

        Components can exist interchangeably and can be within a class/subclass
        system.

2. What is a class?

    A class is a framework within which data (ex. attributes) and behaviors 
    (ex. methods) may be contained. Like strings or files, classes are a "type"
    of thing. 

3. What is an instance attribute?

    An instance attribute is the category of data related to an object. For example,
    an object may have the attribute "name" and its value may be "Nada." 

4. What is a method?

    A method is the class equivalent of a function. It is a behavior contained within
    a class or subclass. 

5. What is an instance in object orientation?

    An instance is an object. Objects may have attributes. They may also be
    subject to the behavior and/or functionality of a method. 

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is an attribute set for every objected that is instantiated
   in that class. For example, if a class has a class attribute of "hunger = 50,"
   every object that is instantiated in that class will have a hunger attribute
   with the value of 50. You would use this if you want everything instantiated
   in a class to have the same attribute and attribute value. 
   
   An instance attribute, however, is an attribute that is
   borne by the object itself by individual assignment rather than by class-wide
   assignment. For example, an object known as fido can be assigned a name attribute
   with the value 'Fido' on an individual basis rather than at the class level. 


"""


# Parts 2 through 5:
# Create your classes and class methods

################################################################################
# Note:   Since the instructions are always not in descending order with regard 
#         to the code below, the labels for parts and prompts in this file are 
#         also not sequential. 
################################################################################

##################
#Part 2: Prompt 1 
##################
class Students(object):
    """A class for students """

    def __init__(self, first_name, last_name, address, score):
    # When an object is instantiated, it will, per this init, have first_name,
    # last_name and address attributes as follows:
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.score = score
        # These three lines create first_name, last_name and address attributes
        # for any instantiated students
########################
#Part 4
########################

    def student_score(self, score):
      """"Captures student score"""
      score = self.administer()
      # Sets score to output of administer method
      self.score = score
      # Resets the value of the self.score from None to the score output

jasmine = Students('Jasmine', 'Debugger', '0101 Computer Street', None)
jacqui = Students('Jacqui', 'Console', '888 Binary Ave', None)
# Examples of how students would be instantiated using the init; they will 
# take on the attribute values passed in within the parenthesis

########################
#Part 2: Prompt 2 
########################

class Questions(object):
# Creates base class for questions; questions will likely not be instantiated
# at this level but in the subclass below

    def __init__(self, question, answer):
    # This template will be used to create template attributes to be used
    # in later instantiations
        self.question = question
        self.answer = answer

########################
#Part 3: Prompt 2
########################

    def ask_and_evaluate(self, question, answer):
      student_ans = raw_input(question)
      if student_ans == answer:
        return True
      else:
        return False
      
# I initially used: "return raw_input(question) is answer" as a boolean that
# would indicate whether the user's input matched the answer. However, this
# kept producing "False" even when the answer matched. To remedy this,
# I created a conditional within the method. I don't think this is the most
# consice way but it does give the accurate outcome. 
#
# Note:   This method is called using midterm.ask_question(midterm.question, 
#         midterm.answer) below. 

########################
#Part 2: Prompt 3
########################

class Exam(Questions):
# Creates a subclass for exams that borrows from the base questions class.
# Other subclasses could possible include a Homework(Questions) subclass, etc.

    def __init__(self, question, answer, score, name):
      """Subclass init"""
      super(Exam, self).__init__(question, answer)
      # "super" borrows from the base class init
      self.name = name
      # Adds a customized attribute for exams that does not exist in the parent

########################
#Part 3: Prompt 1
########################

    def add_question(self, new_question, new_answer):
      """Adds new_question and new_answer attributes with passed in q's/a's"""
      self.new_question = new_question 
      self.new_answer = new_answer

########################
#Part 3: Prompt 3
########################

    # def administer(self, questions, answers):
    #   """Administer question through ask_and_evaluate method; tracks score"""
    #     qa_dict = dict(zip(questions, answers))
    #     # Takes passed in questions and answers lists and merges them into a 
    #     # dictionary
    #     score = 0
    #     # Created score counter
    #     for key, value in qa_dict.iteritems():
    #     # key = question
    #     # value = answer
    #     # Evaluates each question and answer pair in the dictionary
    #         if self.ask_and_evaluate(key, value) == True:
    #         # Evaluates whether raw_input matches the value (the answer)
    #             score = score + 1
    #             # When true, score is incremented +1
    #     return score
    #     # Returns score

########################
#Part 5
########################

class Quiz(Exam):

    def __init__(self, question, answer, name, score):
      """Sub-subclass init"""
      super(Quiz, self).__init__(question, answer, score, name)
      # "super" borrows from the Exam class init

    def administer(self, questions, answers):
      """Borrows from Exam class administer method"""
      super(Quiz, self).administer(questions, answers)
      # "super" borrows from the Exam class administer method
      self.pass_fail = None

################################################################################
#Note:    I spent a considerable amount of time trying to correct indentation
#         issues with my administer method. When using it in a new, clean
#         sublime window, it works. I've tried converting all indents to spaces,
#         manually spacing four times, and generally aligning everything with 
#         the code and indentation levels before and after this method. All efforts
#         were in vain. 
################################################################################

midterm = Exam('What is the method for adding to a set', '.add()', 'Midterm', None)
# Instantiates midterm with empty lists, per the instructions, for the 
# passed questions and answers

#print midterm.question, midterm.answer, midterm.name
# Prints the values of the question, answer and name attributes for the 
# object midterm

midterm.add_question('What color is the sky?','Blue')
# Utilizes the add_question method for midterm to create new values for 
# the new_question and new_answer attributes 

#print midterm.question, midterm.answer
# Prints the values of the question and answer

#print midterm.ask_and_evaluate(midterm.question, midterm.answer)
# Calls the ask_question method for midterm 

#print midterm.administer([midterm.question, midterm.new_question], [midterm.answer, midterm.new_answer])
# Administers an exam with passed questions

########################
#Part 4
########################

################################################################################
#Note:    I think I'm comfortable creating the class structures but I'd like to
#         revisit how to call methods in functions outside of the class system.
#         I'm not sure the functions below are right (I mirrored some after a 
#         homework assignment we had this past week). 
################################################################################

def take_test(student, exam):
  """Creates a test-taking function (not in a class)"""
  students.init(student)
  # Runs init method for the student
  questions.exam.administer(exam)
  # Administers exame through ask_and_evaluate
  students.student_score(student)
  # Assigns score as value to student_score attribute

def example(student, exam):
  """Creates function to create exam, update questions, creates student, administers test"""
  questions.exam.init(exam)
  # Creates exam
  questions.exam.add_question(exam)
  # Adds questions
  students.init(student)
  # Creates student
  questions.exam.administer(exam)
  # 


