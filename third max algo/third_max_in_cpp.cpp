// 2021-1370
#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>

using namespace std;

int third_Max(vector<int> &nums)
{
  long long first = LLONG_MIN, second = LLONG_MIN, third = LLONG_MIN;

  for (int num : nums)
  {
    if (num > first)
    {
      third = second;
      second = first;
      first = num;
    }
    else if (num > second && num != first)
    {
      third = second;
      second = num;
    }
    else if (num > third && num != second)
    {
      third = num;
    }
  }
  return third == LLONG_MIN ? first : third;
}
int main()
{
  vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2};
  int third_max = third_Max(nums);
  cout << "Third maximum number\n=> " << third_max << endl;
  return 0;
}

void BubbleSort(int arr[], int size)
{
  for (int i = 0; i < size; i++)
  {
    for (int j = i + 1; j < size; j++)
    {
      if (arr[i] > arr[j])
      {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
      }
    }
  }
}

int getThirdMax(int arr[], int size)
{
  int max = NEGATIVE_INFINITY;
  int secondMax = NEGATIVE_INFINITY;
  int thirdMax = NEGATIVE_INFINITY;

  for (int i = 0; i < size; i++)
  {
    if (arr[i] > max)
    {
      thirdMax = secondMax;
      secondMax = max;
      max = arr[i];
    }
    else if (arr[i] > secondMax && arr[i] < max)
    {
      thirdMax = secondMax;
      secondMax = arr[i];
    }
    else if (arr[i] > thirdMax && arr[i] < secondMax)
    {
      thirdMax = arr[i];
    }
  }

  return thirdMax;
}
int main()
{
  int arr_1[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2};
  int len1 = sizeof(arr_1) / sizeof(int);
  int first = getThirdMax(arr_1, len1);
}

int getThirdMax1(int arr[], int size)
{
  BubbleSort(arr, size);
  if (size < 3)
    return arr[0];
  return arr[size - 3];
}
int showgetThirdMax1()
{
  int arr_1[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2};
  int len1 = sizeof(arr_1) / sizeof(int);
  int thirdmax1 = getThirdMax1(arr_1, len1);
  cout << "The Third Max is\n =>"<< thirdmax1 << endl;
  return 0;
}

