#include <iostream>

using namespace std;

void partitions(int target, int curr, int* array, int idx)
{
    if (curr + array[idx] == target)
    {
        for (int i=0; i <= idx; i++)
            cout << array[i] << " ";
        cout << endl;
        return;
    }
    else if (curr + array[idx] > target)
    {
        return;
    }
    else
    {
        for(int i = array[idx]+1; i < target; i++)
        {
            array[idx+1] = i;
            partitions(target, curr + array[idx], array, idx+1);
        }
    }
}

int main(){
    int array[100];
    int N = 75;
    for(int i = 1; i < N; i++)
    {
        array[0] = i;
        partitions(N, 0, array, 0);
    }
}
