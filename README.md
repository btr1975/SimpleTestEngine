# Python Script: SimpleTestEngine

## Written By: Benjamin P. Trachtenberg 

### Contact Information:  e_ben_75-python@yahoo.com
### If you have any questions e-mail me

### LinkedIn: [Ben Trachtenberg](https://www.linkedin.com/in/ben-trachtenberg-3a78496)
### Docker Hub: [Docker Hub](https://hub.docker.com/r/btr1975)

### Requirements

* directories==1.0.7
* persistentdatatools==2.2.8
* PyYAML==4.2b4
* menusys==1.1.5

### Languages

* Python

### About

This is a simple test engine you can use for multiple choice, and direct answer.

### YML File Formatting

```yml
--- # Name of question sets Version: 1.0.0
question_sets:
    -   question_set: Midwest
        questions:
        -   question: What is the state capital of Minnesota
            answer: Saint Paul
            answer_opts: <--- With this key included you are making a multiple choice
            -   Burnsville
            -   Saint Paul <--- One answer must match the answer of your question
            -   Minneapolis
            -   Golden Valley
            feedback: <--- This key is not required, if you include it you must inlude the 2 feedback keys
                correct_answer: That is correct good job!
                incorrect_answer: Sorry that is not a correct answer.
                
        -   question: What is the state capital of Minnesota
            answer: <--- Making this a list will make a typed answer with multiple possible matches
            -   Saint Paul
            -   St. Paul
            -   St Paul
            feedback:
                correct_answer: That is correct good job!
                incorrect_answer: Sorry that is not a correct answer.  The correct anser is Saint Paul.

        -   question: What is the state capital in Miisouri
            answer: Jefferson City  <--- Making this a single item means it must match exactly
            feedback:
                correct_answer: That is correct good job!
                incorrect_answer: Sorry that is not a correct answer.
                
    -   question_set: Northeast
        questions:
        -   question: What is the state capital of Maine
            answer: Augusta
            feedback:
                correct_answer: That is correct good job!
                incorrect_answer: Sorry that is not a correct answer.  The correct answer is Augusta.

        -   question: What is the state capital of Connecticut
            answer: Hartford
            answer_opts:
            -   Providence
            -   Hartford
            -   Harrisburg
            -   Boston
            feedback:
                correct_answer: That is correct good job!
                incorrect_answer: Sorry that is not a correct answer.  The correct answer is Hartford.

```
