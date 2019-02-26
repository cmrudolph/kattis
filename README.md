**10 Kinds of People | C** | [Problem](https://open.kattis.com/problems/10kindsofpeople) | [Solution](c/10kindsofpeople.c)</br>
Use a queue and iterative search to identify which cells are connected to each other. A recursive solution is problematic because it can overflow the stack given the right inputs. Once we have tagged contiguous sections of like cells we are prepared to give answers to connectivity questions.
</br></br>
**10 Kinds of People | Python** | [Problem](https://open.kattis.com/problems/10kindsofpeople) | [Solution](py/10kindsofpeople.py)</br>
Use a queue and iterative search to identify which cells are connected to each other. A recursive solution is problematic because it can overflow the stack given the right inputs. Once we have tagged contiguous sections of like cells we are prepared to give answers to connectivity questions. This is the same as the solution implemented in C, but the Python version runs too slowly.
</br></br>
**ACM Contest Scoring | Python** | [Problem](https://open.kattis.com/problems/acm) | [Solution](py/acm.py)</br>
Simple problem with no significant performance requirements.
</br></br>
**ASCII Figure Rotation | Python** | [Problem](https://open.kattis.com/problems/asciifigurerotation) | [Solution](py/asciifigurerotation.py)</br>
Straightforward 2D array manipulation problem where we must adjust both coordinates and values by applying a 90 degree rotation to the source values.
</br></br>
**Adding Words | Python** | [Problem](https://open.kattis.com/problems/addingwords) | [Solution](py/addingwords.py)</br>
Use dictionaries to provide a two-way lookup (values by terms and terms by values). Each of the three instructions is handled per the rules of the problem.
</br></br>
**Almost Perfect | Go** | [Problem](https://open.kattis.com/problems/almostperfect) | [Solution](go/almostperfect.go)</br>
Compute all factor pairs of the specified value using a division test. The factors are then summed and compared to the original value to determine which conclusion is most relevant (exact, almost, none).
</br></br>
**Anagram Counting | Python** | [Problem](https://open.kattis.com/problems/anagramcounting) | [Solution](py/anagramcounting.py)</br>
Calculate the total as n! / (n<sub>1</sub>!n<sub>2</sub>!...n<sub>k</sub>!) where the denominator is the product of the factorials of the number of occurrences of each distinct character in the input sequence.
</br></br>
**Balanced Diet | C** | [Problem](https://open.kattis.com/problems/balanceddiet) | [Solution](c/balanceddiet.c)</br>
Use recursion to figure out all the possible sums we can encounter by combining values in all possible ways. Without any optimizations this solution is O(2<sup>N</sup>). However, the problem is conducive to dynamic programming since once a subproblem has been solved we can save the result leverage it to avoid redundant work.
</br></br>
**Batter Up | Python** | [Problem](https://open.kattis.com/problems/batterup) | [Solution](py/batterup.py)</br>
Use a list comprehension to map strings to integers then do simple math on the list.
</br></br>
**Bit by Bit | Go** | [Problem](https://open.kattis.com/problems/bitbybit) | [Solution](go/bitbybit.go)</br>
Read and process each instruction, modifying the bits as we go.
</br></br>
**CD | C++** | [Problem](https://open.kattis.com/problems/cd) | [Solution](cpp/cd.cpp)</br>
Simple solution involving walking both arrays simultaneously and looking for distinct/duplicates along the way. Chose C++ over Python because the latter was too slow.
</br></br>
**CD | Python** | [Problem](https://open.kattis.com/problems/cd) | [Solution](py/cd.py)</br>
Simple solution involving walking both arrays simultaneously and looking for distinct/duplicates along the way. Python is too slow on official machines.
</br></br>
**Calculator | Python** | [Problem](https://open.kattis.com/problems/calculator) | [Solution](py/calculator.py)</br>
Leverage Python's eval function to make this simple.
</br></br>
**Counting Stars | Python** | [Problem](https://open.kattis.com/problems/countingstars) | [Solution](py/countingstars.py)</br>
Similar problem to amoebas, but recursion grew the stack too much. Using iteration with a queue to visit and tag cells instead.
</br></br>
**DRM Messages | Python** | [Problem](https://open.kattis.com/problems/drmmessages) | [Solution](py/drmmessages.py)</br>
Straightforward application of the string manipulation rules. No performance constraints, so Python is adequate.
</br></br>
**Dance Recital | C++** | [Problem](https://open.kattis.com/problems/dancerecital) | [Solution](cpp/dancerecital.cpp)</br>
Brute forcing all permutations is viable because N is small enough. Chose C++ over Python because the latter was too slow.
</br></br>
**Dance Recital | Python** | [Problem](https://open.kattis.com/problems/dancerecital) | [Solution](py/dancerecital.py)</br>
Brute forcing all permutations is viable because N is small enough. Python is too slow on official machines.
</br></br>
**Eb Alto Saxophone Player | Python** | [Problem](https://open.kattis.com/problems/saxophone) | [Solution](py/saxophone.py)</br>
Simple problem.
</br></br>
**Engineering English | Go** | [Problem](https://open.kattis.com/problems/engineeringenglish) | [Solution](go/engineeringenglish.go)</br>
Iterate over the strings in the input and use a map to store values we have seen before. A value's existence in the map means we need to replace it with our token value.
</br></br>
**Foosball Dynasty | Python** | [Problem](https://open.kattis.com/problems/foosball) | [Solution](py/foosball.py)</br>
Problem has no performance requirements, so Python is fine. Work through the rules, maintaining state properly as we go.
</br></br>
**Game of Throwns | Python** | [Problem](https://open.kattis.com/problems/throwns) | [Solution](py/throwns.py)</br>
Simple problem.
</br></br>
**Hello World! | Python** | [Problem](https://open.kattis.com/problems/hello) | [Solution](py/hello.py)</br>
Impossible to mess this one up...
</br></br>
**Hidden Password | Python** | [Problem](https://open.kattis.com/problems/hidden) | [Solution](py/hidden.py)</br>
Simple problem.
</br></br>
**Inverse Factorial | C** | [Problem](https://open.kattis.com/problems/inversefactorial) | [Solution](c/inversefactorial.c)</br>
Special case the first few factorial cases. After that use logs and take advantage of the fact we can identify the answer based on the number of digits in the factorial string.
</br></br>
**Inverse Factorial - Long Division | C** | [Problem](https://open.kattis.com/problems/inversefactorial) | [Solution](c/inversefactorial_longdiv.c)</br>
Use repeated long division. While conceptually sound, this approach is computationally expensive and runs for too long on official judging machines.
</br></br>
**Line Them Up | Python** | [Problem](https://open.kattis.com/problems/lineup) | [Solution](py/lineup.py)</br>
Simple problem.
</br></br>
**Lost in Translation | Python** | [Problem](https://open.kattis.com/problems/lost) | [Solution](py/lost.py)</br>
Interesting graph problem. We traverse the graph using recursion to compute all our costs and then sum them up to determine the overall min.
</br></br>
**Parsing Hex | Python** | [Problem](https://open.kattis.com/problems/parsinghex) | [Solution](py/parsinghex.py)</br>
Extract hex strings using a regex.
</br></br>
**Passing Secrets | Python** | [Problem](https://open.kattis.com/problems/passingsecrets) | [Solution](py/passingsecrets.py)</br>
Undirected, weighted graph problem where we want the shortest route between two specific nodes. Start by building the graph representation of the problem domain based on the inputs. Then apply Dijkstra's algorithm to identify the shortest paths from the starting node to everything else. Finally consult the search results to retrace our steps to get to the end node optimally.
</br></br>
**Permutation Encryption | Go** | [Problem](https://open.kattis.com/problems/permutationencryption) | [Solution](go/permutationencryption.go)</br>
Iterate over the string to 'encrypt' while repeatedly looping over the key string. The key string drives character selection as we build up the result.
</br></br>
**Phone List | Python** | [Problem](https://open.kattis.com/problems/phonelist) | [Solution](py/phonelist.py)</br>
Simple problem.
</br></br>
**Planina | Python** | [Problem](https://open.kattis.com/problems/planina) | [Solution](py/planina.py)</br>
Simple problem.
</br></br>
**Rain Fall | Python** | [Problem](https://open.kattis.com/problems/rainfall2) | [Solution](py/rainfall2.py)</br>
Interesting problem where we piece together the formula, then run a guess through it, compare, and refine the guess. Repeating this enough times gets us to right value for our unknown.
</br></br>
**Red Rover | Python** | [Problem](https://open.kattis.com/problems/redrover) | [Solution](py/redrover.py)</br>
Simple problem.
</br></br>
**Sheba's Amoebas | Python** | [Problem](https://open.kattis.com/problems/amoebas) | [Solution](py/amoebas.py)</br>
Work through the search space using recursion, tagging cells along the way. In principle, recursion can overflow the stack in these types of problems, but the search space here is sufficiently small that it is okay.
</br></br>
**The Calculus of Ada | Python** | [Problem](https://open.kattis.com/problems/ada) | [Solution](py/ada.py)</br>
Simple recursive implementation with no significant performance requirements.
</br></br>
**The Key to Cryptography | Python** | [Problem](https://open.kattis.com/problems/keytocrypto) | [Solution](py/keytocrypto.py)</br>
Straightforward application of the string manipulation rules. No performance constraints, so Python is adequate.
</br></br>
**What does the fox say? | Python** | [Problem](https://open.kattis.com/problems/whatdoesthefoxsay) | [Solution](py/whatdoesthefoxsay.py)</br>
Simple problem.
</br></br>
