This is the Calculator Compiler! Calculators, unless powered by a search engine, usually cannot deal with math related words like <i>one</i> and <i>two</i>. 
As such, I decided to make a parser for both numbers and written numbers, as well as operators like * or <i>times</i>. 
The way it is written, it acts like a rudimentary compiler, hence the name. It compiles down to Python Code. 
Math is very expansive, and right now this just works out of the terminal, so I'll be adding more things as I go, such as a nice interface and error checking.
</br>
<h2>UPDATES: </h2>
</br>
<h3>v1.0:</h3> Added the baselines classes <code>Symbol</code> and <code>Parser</code> in <a href = "processtomath.py"> processtomath.py</a>, basic 
compiling functionality. <a href = "interface.py">interface.py</a> is currently lacking functionality, but contains a demo for how it will be used right now.
</br>
<h3>v1.0.1:</h3> Basic bug fixing. Added numbers 11-19, as well as multiples of 10 from 20-90. Also added non-written numbers to <code>_ABLE_TO_BE_MULTIPLIERS</code>, as that was causing issues with proper multiplication.
</br>
<h2> COMING FEATURES: </h2>
<ul>
  <li>Proper implementation of an terminal-based interface</li>
  <li>Better error handling and more dynamic features</li>
  <li>Revamp of <code>Symbol</code> to be abstract, and have child classes <code>Multiplier</code>, <code>Number</code>, and <code>Operator</code></li>.
 </ul>
