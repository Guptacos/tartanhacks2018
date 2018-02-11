# tartanhacks2018
Repository for our 2018 TartanHacks project

This project was created by:
Niko Gupta nikolasg@andrew.cmu.edu
Logan Kojiro lkojiro@andrew.cmu.edu
Joel Miller jgmiller@andrew.cmu.edu
Haiwen Liu haiwenl@andrew.cmu.edu

The goal of this project is primarily eduational. We hope that our project can
be used to help teach students (of any age and level of expertise) more about
digital circuits.

The main file that you run is GUI.py. When run, it outputs an interface that the
user can interact with. The provided buttons are "live mode", "about", and 
"exit". Exit and about are self explanatory. Live mode opens an interactive
game mode where the user can build circuits and run analysis on them. The
system requires that a webcam is plugged in and pointed at the circuit.

In the live mode, the user can choose to "analyze circuit", which will convert
the circuit they've built into an equation. It will also compute the logically
simplified equation, and output both circuits and equations on the screen.
In addition, there are buttons that allow the user to test inputs and see the
outputs of their circuit. They can also choose to re-analyze the board, which
will reload the page with updated information.

The other files are as follows:

digital_circuit.py      (Joel Miller)
   Class definitions for circuit data structures

gates.py                (Joel Miller)
    Gate class declarations

imagesHandler.py        (Logan Kojiro)
    Takes an image of the board, breaks it up, and then determines which of the
    pictures contains an element. It then passes those images to 
    image_recognition.py for analysis.

image_recognition.py    (Haiwen Liu)
    Given a directory of images, uses Microsoft's Azure Custom Vision to 
    classify each image as a gate, input, or None type, and returns a 2d
    list of the board.

make_circuit.py         (Niko Gupta)
    Given a 2d list representing a board, it recursively generates a circuit
    object. In the initialization of this object, the QM algorithm below is
    called and the output equation is stored in the circuit object.

ourQM.py                (Niko Gupta)
    A file to interface between our representation of circuits and the 
    given representation in the QM library.

qm_files                (Robert Dick)
    A QM algorithm taken from Robert Dick of University of Michigan. 
    See README.txt and license within this folder for further information.

equation_parse.py       (Logan Kojiro)
    Given a boolean expression, and input values, evaluates the truth value 
    of the expression.  Uses this to create a truth table for an arbitrary
    boolean expression.

