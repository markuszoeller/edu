#############
A simple test
#############

Lorem ipsum [Ref]_ dolor sit amet.


=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======


* this is
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues

section B
=========

term (up to a line of text)
   Definition of the term, which must be indented

   and can even consist of multiple paragraphs

next term
   Description.
   
.. code-block:: java
   :linenos:

   public static void main(String[] args) {
      system.out.println("hello world") 
   }

section C
=========

.. literalinclude:: /code/Foo.java
   :language: java
   :emphasize-lines: 3
   :linenos:

section D
=========

.. glossary::
   :sorted:

   environment
      A structure where information about all documents under the root is
      saved, and used for cross-referencing.  The environment is pickled
      after the parsing stage, so that successive runs only need to read
      and parse new and changed documents.

   source directory
      The directory which, including its subdirectories, contains all
      source files for one Sphinx project.
      
   asdf
      The asdf of the lorem with the bar and ipsum


References
==========

.. [Ref] Book or article reference, URL or whatever.