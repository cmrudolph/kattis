// https://open.kattis.com/problems/cd

#include <iostream>

using namespace std;

int main()
{
    int n;
    int m;
    int jack;
    int jill;

    ios::sync_with_stdio(false);

    cin >> n >> m;
    while (n > 0 || m > 0)
    {
        int duplicates = 0;

        int* jack_list = new int[n];
        int* jill_list = new int[m];

        for (int i = 0; i < n; i++)
        {
            cin >> jack_list[i];
        }
        for (int i = 0; i < m; i++)
        {
            cin >> jill_list[i];
        }

        int jack_idx = 0;
        int jill_idx = 0;

        while (jack_idx < n || jill_idx < m)
        {
            int jack = jack_list[jack_idx];
            int jill = jill_list[jill_idx];

            if (jack == jill)
            {
                duplicates++;
                jack_idx++;
                jill_idx++;
            }
            else if (jack < jill)
            {
                jack_idx++;
            }
            else
            {
                jill_idx++;
            }
        }

        delete jack_list;
        delete jill_list;

        cout << duplicates << endl;
        cin >> n >> m;
    }
}
