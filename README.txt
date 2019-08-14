=============
CrackTheFlag
=============
*A module-based CTF framework and exploit development library written in Python 3.7, meant to automate tedious tasks and rapidly prototype exploits for use during CTF challenges*

Typical Usage Includes:: python

    #!/usr/bin/env python
     
    from ctf import ctflib
    
    c = ctf.ctflib.crytpto.caesar()

To-Do
-----
* `[ ]` Create a development page to allow other people to help contribute to the project (*PyPy, Github*)
* `[ ]` Restructure the file setup to make it more versatile
* `[ ]` Get basic modules like data handling that can be used in other modules
* `[ ]` Modules to interact with websites and shells dynamically

End Goals
---------
1. Create a standard library with accessible modules to use while scripting
2. Create a **text-editor/REPL** hybrid with a custom lexer for automatic syntax hightlighting, autocompletion, etc.
3. Provide a framework to solve any CTF problem

Pwntools *vs.* CrackTheFlag
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Although it mostly sounds like this project is a straight rip of pwntools, there are a few **key** differences between the two:: 

    1.) Includes: the standard library, as well as the text-editor
    2.) Includes a REPL for testing modules and working with CrackTheFlag independently
    3.) Written in Python 3.7, limited backwards compatibility
    4.) Featured in an upcoming project :^)