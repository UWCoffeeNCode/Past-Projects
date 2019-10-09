# Glossary

### Game Loop
The game loop is the heart of any game. Fundamentally, it is a function which runs continuously, creating the game frame-by-frame.

During each iteration of the game loop function, there are different phases, each modifying the game in a special way.
The phases are **initialization**, **updating**, and **drawing**.

1. **Initialization:** In this phase, game setups (from configuration files) are run, and the environment is prepared for the draw and
update phases. This can include creating the entities (characters and items) and loading the physics engine.
2. **Updating:** During this phase, all the objects in the game are prepared to be drawn. This can include taking in
player inputs and moving the character accordingly. Or, if any combat occurred, the amount of health points remaining 
may need to be adjusted.
3. **Drawing:** All the changes that occur in the updating phase must now be represented visually (or by audio). During
the drawing phase, the character is redrawn to a different position, the health bar reflects the change in health, and
the current score is perhaps updated.

![The game loop](http://openbookproject.net/thinkcs/python/english3e/_images/pygame_structure.png)

### Module
Simply put, a module is a file consisting of Python code (can be other programming languages, as well).
A module usually is a collection of variables, functions, and class definitions, which are used for common or coherent
purposes. The are organized in a file together so they can be imported (brought into your work), as needed, in multiple
locations.

**NOTE:** When programming in python, for a `.py` file to be considered a module, the directory (folder) containining that
file must also containa file named `__init__.py`.

### Root Directory

The root directory is the first or top-most directory in a hierarchy. When someone refers to the
*root directory of a project*, they mean the folder which contains all the files and folders of a project.
