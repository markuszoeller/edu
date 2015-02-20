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


.. [Ref] Book or article reference, URL or whatever.