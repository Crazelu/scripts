import "dart:io";
/**Given an array A of n integers, and a value X, your task is the count the number of subsequences of the given array having a total bitwise OR value of .

A subsequence of an array can be derived by deleting all, some or none of the elements of the array without changing the order of the remaining elements. Reference: Subsequences.

A bitwise OR is a binary operation that takes two bit patterns of equal length and performs the logical inclusive OR operation on each pair of corresponding bits. Reference: Bitwise OR.

NOTE: The problem asks for subsequences, not subarrays!

Input Format

The first line contains two integers  and .

The second line contains  integers, , representing the values in the array.

Output Format

The output should contain one line, the number of sequences of the array with bitwise OR equal to X.
https://www.hackerrank.com/contests/adorahack-dsa-challenge-1/challenges/subsequences-with-or
**/

// void main() {
//   subsequences(5, 2, [3, 1, 2, 4, 2]);
// }

// void subsequences(int n, int x, List<int> array){
// int count = 0;
// array.sort((a,b)=> a.compareTo(b));

// int temp = array[0];
// for(int i =0; i< n; i++){
//   for(int j =i+1; j<n; j++){
//     if(array[j] == x) count++;
//     if((temp|array[j])==x){
//        temp = x;
//       count++;
//     }
//     else {
//       temp = array[j];
//       break;
//     }
//   }
// }
//   print(count);
// }

void main() {
  final args = List<int>.from(stdin.readLineSync()!.split(" ").map(int.parse));
  final array = List<int>.from(stdin.readLineSync()!.split(" ").map(int.parse));
  subsequences(args[0], args[1], array);
}

void subsequences(int n, int x, List<int> array) {
  int passes = n;
  int count = 0;

  while (passes >= 2) {
    count += solve(passes, x, array, n);
    passes--;
  }

  print(count);
}

int solve(int n, int x, List<int> array, int length) {
  int passes = n;
  int count = 0;
  if (length == n) {
    array.forEach((e) {
      if (e == x) {
        count++;
      }
    });

    int temp = array[0];
    for (int i = 1; i <= n - 1; i++) {
      temp = temp | array[i];
      if (temp == x)
        count++;
      else
        break;
    }

    return count;
  }

  int i = -1;

  while (passes >= 2) {
    i++;
    int j = length - 1;

    int temp = array[i] | array[j];
    if (temp == x) count++;

    while (j > i + 1) {
      j--;
      temp = array[i] | array[j];
      if (temp == x)
        count++;
      else
        break;
    }

    passes--;
  }

  return count;
}
