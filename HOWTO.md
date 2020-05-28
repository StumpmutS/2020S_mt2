# HOWTO work these questions

There are three questions: 

* Q1:  Calculate the (minimum) height of a tree. 
       Starter code is in 
       [`q1_tree_height.py`](q1_tree_height.py).
       See [Howto Q1 Tree Height](doc/HOWTO_q1_tree_depth.md)
       
* Q2: Pack and unpack unsigned integer bit fields
      in a 16-bit word.  
      Starter code is in 
      [`q2_bits.py`](q2_bits.py). 
      See 
      [HOWTO pack](doc/HOWTO_q2_bits.md)
      
* Q3: Determine whether at least one column 
      of a grid includes all the colors in 
      a given list of colors.  
      Starter code is in 
      [`q3_logic.py`](q3_logic.py). 
      See 
      [HOWTO check all the colors](doc/HOWTO_q3_logic.md)
      
# Addenda

After the exam, I have added new variations to 
Q3:  
* All columns all colors, 
* some column distinct colors, and 
* all rows distinct colors.  

These are exercises to further practice solving any/all and 
row/column type questions.  I suggest using sets, 
but for small grids a solution using only lists can 
also be efficient.  (For large grids, say beyond 
100 x 100, using lists will be much slower than using
sets.)

While determining whether a column uses all the colors
of a spectrum is not a very realistic problem, it is a
simple example of a kind of problem that does come up
often in practice, which is determining whether certain 
traversals of a data structure have some particular 
pattern.  For example, there is a "two phase"
property that we expect of paths that packets take in the 
internet, first moving to larger and larger routers, 
then to smaller and smaller routers. 