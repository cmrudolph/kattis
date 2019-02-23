// NAME : Dance Recital
// URL  : https://open.kattis.com/problems/dancerecital
// =============================================================================
// Brute forcing all permutations is viable because N is small enough. Chose
// C++ over Python because the latter was too slow.
// =============================================================================

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_ROUTINES = 10;
const int MAX_PERFORMERS = 26;

// Figure out how many character differences exist between two strings
int diffs(string s1, string s2)
{
    int result = 0;

    for (int i = 0; i < s1.length(); i++)
    {
        for (int j = 0; j < s2.length(); j++)
        {
            if (s1[i] == s2[j])
            {
                result++;
            }
        }
    }

    return result;
}

int main()
{
    int n;
    string str;
    vector<string> routines;

    int distances[MAX_ROUTINES][MAX_ROUTINES] = {0};

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> str;
        routines.push_back(str);
    }

    // Precalculate all the differenes between all string combinations. We won't
    // technically use them all (we are only searching half the permutations), but
    // this is cheap.
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            int num_diffs = diffs(routines[i], routines[j]);
            distances[i][j] = num_diffs;
            distances[j][i] = num_diffs;
        }
    }

    int ints[MAX_ROUTINES] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    int first_idx = 0;
    int last_idx = n - 1;
    int best = 123123123;

    do
    {
        if (ints[first_idx] < ints[last_idx])
        {
            // Only consider half the permutations. If a sequence is a mirror image
            // of one we have already processed, the result will be the same and we
            // can skip it.
            int changes = 0;
            for (int i = 0; i < n - 1; i++)
            {
                changes += distances[ints[i]][ints[i+1]];
                if (changes >= best)
                {
                    break;
                }
            }

            if (changes < best)
            {
                best = changes;
            }
        }
    } while(next_permutation(ints, ints + n));

    cout << best << endl;
}