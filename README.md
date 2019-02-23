**10 Kinds of People | C** | [Problem](https://open.kattis.com/problems/10kindsofpeople) | [Solution](c/10kindsofpeople.c)</br>
Use a queue and iterative search to identify which cells are connected to each other. A recursive solution is problematic because it can overflow the stack given the right inputs. Once we have tagged contiguous sections of like cells we are prepared to give answers to connectivity questions.
</br></br>
**Almost Perfect | Go** | [Problem](https://open.kattis.com/problems/almostperfect) | [Solution](go/almostperfect.go)</br>
Compute all factor pairs of the specified value using a division test. The factors are then summed and compared to the original value to determine which conclusion is most relevant (exact, almost, none).
</br></br>
**Balanced Diet | C** | [Problem](https://open.kattis.com/problems/balanceddiet) | [Solution](c/balanceddiet.c)</br>
Use recursion to figure out all the possible sums we can encounter by combining values in all possible ways. Without any optimizations this solution is O(2<sup>N</sup>). However, the problem is conducive to dynamic programming since once a subproblem has been solved we can save the result leverage it to avoid redundant work.
</br></br>
**Balanced Diet | C#** | [Problem](https://open.kattis.com/problems/balanceddiet) | [Solution](cs/balanceddiet.cs)</br>
Use recursion to figure out all the possible sums we can encounter by combining values in all possible ways. Without any optimizations this solution is O(2<sup>N</sup>). However, the problem is conducive to dynamic programming since once a subproblem has been solved we can save the result leverage it to avoid redundant work. Solved in C# to compare language performance versus C on judging machines.
</br></br>
**Bit by Bit | Go** | [Problem](https://open.kattis.com/problems/bitbybit) | [Solution](go/bitbybit.go)</br>
Read and process each instruction, modifying the bits as we go.
</br></br>
**CD | C++** | [Problem](https://open.kattis.com/problems/cd) | [Solution](cpp/cd.cpp)</br>
Simple solution involving walking both arrays simultaneously and looking for distinct/duplicates along the way. Chose C++ over Python because the latter was too slow.
</br></br>
**Dance Recital | C++** | [Problem](https://open.kattis.com/problems/dancerecital) | [Solution](cpp/dancerecital.cpp)</br>
Brute forcing all permutations is viable because N is small enough. Chose C++ over Python because the latter was too slow.
</br></br>
**Engineering English | Go** | [Problem](https://open.kattis.com/problems/engineeringenglish) | [Solution](go/engineeringenglish.go)</br>
Iterate over the strings in the input and use a map to store values we have seen before. A value's existence in the map means we need to replace it with our token value.
</br></br>
**Inverse Factorial | C** | [Problem](https://open.kattis.com/problems/inversefactorial) | [Solution](c/inversefactorial.c)</br>
Special case the first few factorial cases. After that use logs and take advantage of the fact we can identify the answer based on the number of digits in the factorial string.
</br></br>
**Inverse Factorial - Long Division | C** | [Problem](https://open.kattis.com/problems/inversefactorial) | [Solution](c/inversefactorial_longdiv.c)</br>
Use repeated long division. While conceptually sound, this approach is computationally expensive and runs for too long on official judging machines.
</br></br>
**Permutation Encryption | Go** | [Problem](https://open.kattis.com/problems/permutationencryption) | [Solution](go/permutationencryption.go)</br>
Iterate over the string to 'encrypt' while repeatedly looping over the key string. The key string drives character selection as we build up the result.
</br></br>
