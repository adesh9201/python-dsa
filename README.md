# 🧠 Data Structures & Algorithms (DSA) in Python

A comprehensive roadmap to master Data Structures and Algorithms using Python. Each topic includes theoretical references, Python implementations, and practice problems to build strong problem-solving skills.

## 🎯 About This Repository

This repository is designed for:
- **Beginners** starting their DSA journey
- **Intermediate learners** strengthening their concepts
- **Interview preparation** for tech companies
- **Competitive programming** enthusiasts

## 📚 Table of Contents

1. [Arrays](#1--arrays)
2. [Strings](#2--strings)
3. [Linked Lists](#3--linked-lists)
4. [Stacks & Queues](#4--stacks--queues)
5. [Hashing](#5--hashing)
6. [Recursion & Backtracking](#6--recursion--backtracking)
7. [Searching & Sorting](#7--searching--sorting)
8. [Greedy Algorithms](#8--greedy-algorithms)
9. [Dynamic Programming](#9--dynamic-programming)
10. [Trees](#10--trees)
11. [Graphs](#11--graphs)
12. [Bit Manipulation](#12--bit-manipulation)

---

## 1. 📦 Arrays

Arrays are fundamental data structures that store elements in contiguous memory locations.

| Topic | Theory | Code Example | Difficulty |
|-------|--------|--------------|------------|
| Array Basics & Traversals | [Learn Arrays](https://www.geeksforgeeks.org/array-data-structure/) | [`arrays/basics.py`](arrays/basics.py) | 🟢 Easy |
| Two Pointer Technique | [Two Pointers](https://www.geeksforgeeks.org/two-pointers-technique/) | [`arrays/two_pointers.py`](arrays/two_pointers.py) | 🟡 Medium |
| Kadane's Algorithm | [Maximum Subarray](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/) | [`arrays/kadane.py`](arrays/kadane.py) | 🟡 Medium |
| Prefix Sum | [Prefix Sum Array](https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/) | [`arrays/prefix_sum.py`](arrays/prefix_sum.py) | 🟡 Medium |
| Sliding Window | [Sliding Window](https://www.geeksforgeeks.org/window-sliding-technique/) | [`arrays/sliding_window.py`](arrays/sliding_window.py) | 🟡 Medium |

**Key Problems:** Maximum Subarray, Two Sum, Three Sum, Container With Most Water

---

## 2. 🔤 Strings

String manipulation and pattern matching algorithms.

| Topic | Theory | Code Example | Difficulty |
|-------|--------|--------------|------------|
| String Operations | [Python Strings](https://docs.python.org/3/tutorial/introduction.html#strings) | [`strings/operations.py`](strings/operations.py) | 🟢 Easy |
| Palindromes | [Palindrome Check](https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/) | [`strings/palindrome.py`](strings/palindrome.py) | 🟢 Easy |
| Anagrams | [Anagram Check](https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/) | [`strings/anagrams.py`](strings/anagrams.py) | 🟡 Medium |
| KMP Algorithm | [Pattern Matching](https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/) | [`strings/kmp.py`](strings/kmp.py) | 🔴 Hard |

**Key Problems:** Valid Palindrome, Longest Palindromic Substring, Group Anagrams

---

## 3. 🔗 Linked Lists

Linear data structures with dynamic memory allocation.

| Topic | Theory | Code Example | Difficulty |
|-------|--------|--------------|------------|
| Singly Linked List | [Singly LL](https://www.geeksforgeeks.org/data-structures/linked-list/singly-linked-list/) | [`linked_list/singly.py`](linked_list/singly.py) | 🟢 Easy |
| Doubly Linked List | [Doubly LL](https://www.geeksforgeeks.org/data-structures/linked-list/doubly-linked-list/) | [`linked_list/doubly.py`](linked_list/doubly.py) | 🟡 Medium |
| Reverse Linked List | [Reverse LL](https://www.geeksforgeeks.org/reverse-a-linked-list/) | [`linked_list/reverse.py`](linked_list/reverse.py) | 🟡 Medium |
| Cycle Detection | [Floyd's Algorithm](https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/) | [`linked_list/cycle_detection.py`](linked_list/cycle_detection.py) | 🟡 Medium |
| Merge Two Sorted Lists | [Merge Lists](https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/) | [`linked_list/merge_sorted.py`](linked_list/merge_sorted.py) | 🟡 Medium |

**Key Problems:** Reverse Linked List, Merge Two Sorted Lists, Linked List Cycle

---

## 4. 📚 Stacks & Queues

LIFO and FIFO data structures for various applications.

| Topic | Theory | Code Example | Difficulty |
|-------|--------|--------------|------------|
| Stack Implementation | [Stack in Python](https://www.geeksforgeeks.org/stack-in-python/) | [`stacks_queues/stack.py`](stacks_queues/stack.py) | 🟢 Easy |
| Queue Implementation | [Queue in Python](https://www.geeksforgeeks.org/queue-in-python/) | [`stacks_queues/queue.py`](stacks_queues/queue.py) | 🟢 Easy |
| Valid Parentheses | [Balanced Parentheses](https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/) | [`stacks_queues/valid_parentheses.py`](stacks_queues/valid_parentheses.py) | 🟡 Medium |
| Next Greater Element | [NGE](https://www.geeksforgeeks.org/next-greater-element/) | [`stacks_queues/next_greater.py`](stacks_queues/next_greater.py) | 🟡 Medium |

**Key Problems:** Valid Parentheses, Min Stack, Next Greater Element

---

## 5. 🔐 Hashing

Hash tables and hash maps for efficient data retrieval.

| Topic | Theory | Code Example | Difficulty |
|-------|--------|--------------|------------|
| HashMap Basics | [Hash Tables](https://www.geeksforgeeks.org/hashing-data-structure/) | [`hashing/basics.py`](hashing/basics.py) | 🟢 Easy |
| Frequency Counting | [Count Frequencies](https://www.geeksforgeeks.org/counting-frequencies-of-array-elements/) | [`hashing/frequency.py`](hashing/frequency.py) | 🟢 Easy |
| Hash Set Operations | [Set Operations](https://www.geeksforgeeks.org/sets-in-python/) | [`hashing/set_operations.py`](hashing/set_operations.py) | 🟡 Medium |
| Collision Handling | [Collision Resolution](https://www.geeksforgeeks.org/hashing-set-3-open-addressing/) | [`hashing/collision_handling.py`](hashing/collision_handling.py) | 🟡 Medium |

**Key Problems:** Two Sum, Group Anagrams, Longest Consecutive Sequence

---

## 6. 🌀 Recursion & Backtracking

Problem-solving techniques using recursive approaches.

| Topic | Theory | Code Example | Difficulty |
|-------|--------|--------------|------------|
| Recursion Basics | [Recursion](https://www.geeksforgeeks.org/recursion/) | [`recursion/basics.py`](recursion/basics.py) | 🟢 Easy |
| N-Queens Problem | [N Queens](https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/) | [`recursion/nqueens.py`](recursion/nqueens.py) | 🔴 Hard |
| Sudoku Solver | [Sudoku](https://www.geeksforgeeks.org/sudoku-backtracking-7/) | [`recursion/sudoku.py`](recursion/sudoku.py) | 🔴 Hard |
| Permutations | [Generate Permutations](https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/) | [`recursion/permutations.py`](recursion/permutations.py) | 🟡 Medium |
| Combinations | [Generate Combinations](https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/) | [`recursion/combinations.py`](recursion/combinations.py) | 🟡 Medium |

**Key Problems:** Generate Parentheses, Word Search, Palindrome Partitioning

---

## 7. 🔍 Searching & Sorting

Essential algorithms for data organization and retrieval.

| Topic | Theory | Code Example | Difficulty |
|-------|--------|--------------|------------|
| Linear Search | [Linear Search](https://www.geeksforgeeks.org/linear-search/) | [`search_sort/linear_search.py`](search_sort/linear_search.py) | 🟢 Easy |
| Binary Search | [Binary Search](https://www.geeksforgeeks.org/binary-search/) | [`search_sort/binary_search.py`](search_sort/binary_search.py) | 🟡 Medium |
| Bubble Sort | [Bubble Sort](https://www.geeksforgeeks.org/bubble-sort/) | [`search_sort/bubble_sort.py`](search_sort/bubble_sort.py) | 🟢 Easy |
| Quick Sort | [Quick Sort](https://www.geeksforgeeks.org/quick-sort/) | [`search_sort/quick_sort.py`](search_sort/quick_sort.py) | 🟡 Medium |
| Merge Sort | [Merge Sort](https://www.geeksforgeeks.org/merge-sort/) | [`search_sort/merge_sort.py`](search_sort/merge_sort.py) | 🟡 Medium |
| Heap Sort | [Heap Sort](https://www.geeksforgeeks.org/heap-sort/) | [`search_sort/heap_sort.py`](search_sort/heap_sort.py) | 🔴 Hard |

**Key Problems:** Search in Rotated Sorted Array, Find Peak Element, Kth Largest Element

---

## 8. 💰 Greedy Algorithms

Algorithms that make locally optimal choices at each step.

| Topic | Theory | Code Example | Difficulty |
|-------|--------|--------------|------------|
| Activity Selection | [Activity Selection](https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/) | [`greedy/activity_selection.py`](greedy/activity_selection.py) | 🟡 Medium |
| Fractional Knapsack | [Fractional Knapsack](https://www.geeksforgeeks.org/fractional-knapsack-problem/) | [`greedy/fractional_knapsack.py`](greedy/fractional_knapsack.py) | 🟡 Medium |
| Huffman Coding | [Huffman Coding](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/) | [`greedy/huffman_coding.py`](greedy/huffman_coding.py) | 🔴 Hard |
| Job Scheduling | [Job Scheduling](https://www.geeksforgeeks.org/job-sequencing-problem/) | [`greedy/job_scheduling.py`](greedy/job_scheduling.py) | 🟡 Medium |

**Key Problems:** Jump Game, Gas Station, Minimum Number of Arrows

---

## 9. 🧮 Dynamic Programming

Optimization technique using overlapping subproblems and optimal substructure.

| Topic | Theory | Code Example | Difficulty |
|-------|--------|--------------|------------|
| Fibonacci DP | [Memoization](https://www.geeksforgeeks.org/dynamic-programming/) | [`dp/fibonacci.py`](dp/fibonacci.py) | 🟢 Easy |
| 0/1 Knapsack | [Knapsack Problem](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/) | [`dp/knapsack.py`](dp/knapsack.py) | 🟡 Medium |
| Longest Common Subsequence | [LCS](https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/) | [`dp/lcs.py`](dp/lcs.py) | 🟡 Medium |
| Coin Change | [Coin Change](https://www.geeksforgeeks.org/coin-change-dp-7/) | [`dp/coin_change.py`](dp/coin_change.py) | 🟡 Medium |
| Edit Distance | [Edit Distance](https://www.geeksforgeeks.org/edit-distance-dp-5/) | [`dp/edit_distance.py`](dp/edit_distance.py) | 🔴 Hard |

**Key Problems:** House Robber, Maximum Product Subarray, Unique Paths

---

## 10. 🌳 Trees

Hierarchical data structures with various traversal and manipulation techniques.

| Topic | Theory | Code Example | Difficulty |
|-------|--------|--------------|------------|
| Binary Tree Basics | [Binary Trees](https://www.geeksforgeeks.org/binary-tree-data-structure/) | [`trees/binary_tree.py`](trees/binary_tree.py) | 🟢 Easy |
| Tree Traversals | [Tree Traversals](https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/) | [`trees/traversals.py`](trees/traversals.py) | 🟡 Medium |
| Binary Search Tree | [BST](https://www.geeksforgeeks.org/binary-search-tree-data-structure/) | [`trees/bst.py`](trees/bst.py) | 🟡 Medium |
| AVL Tree | [AVL Tree](https://www.geeksforgeeks.org/avl-tree-set-1-insertion/) | [`trees/avl_tree.py`](trees/avl_tree.py) | 🔴 Hard |
| Trie | [Trie Data Structure](https://www.geeksforgeeks.org/trie-insert-and-search/) | [`trees/trie.py`](trees/trie.py) | 🟡 Medium |

**Key Problems:** Maximum Depth of Binary Tree, Validate BST, Lowest Common Ancestor

---

## 11. 🌐 Graphs

Networks of vertices and edges with various algorithms for traversal and optimization.

| Topic | Theory | Code Example | Difficulty |
|-------|--------|--------------|------------|
| Graph Representation | [Graph Basics](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/) | [`graphs/representation.py`](graphs/representation.py) | 🟢 Easy |
| BFS & DFS | [Graph Traversal](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/) | [`graphs/bfs_dfs.py`](graphs/bfs_dfs.py) | 🟡 Medium |
| Dijkstra's Algorithm | [Shortest Path](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/) | [`graphs/dijkstra.py`](graphs/dijkstra.py) | 🔴 Hard |
| Kruskal's Algorithm | [MST](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/) | [`graphs/kruskal.py`](graphs/kruskal.py) | 🔴 Hard |
| Topological Sort | [Topological Sorting](https://www.geeksforgeeks.org/topological-sorting/) | [`graphs/topological_sort.py`](graphs/topological_sort.py) | 🟡 Medium |

**Key Problems:** Number of Islands, Clone Graph, Course Schedule

---

## 12. ⚙️ Bit Manipulation

Efficient operations using bitwise operators.

| Topic | Theory | Code Example | Difficulty |
|-------|--------|--------------|------------|
| Bitwise Operations | [Bitwise Operators](https://www.geeksforgeeks.org/bitwise-operators-in-python/) | [`bitwise/basics.py`](bitwise/basics.py) | 🟢 Easy |
| Power of Two | [Check Power of 2](https://www.geeksforgeeks.org/program-to-find-whether-a-no-is-power-of-two/) | [`bitwise/power_of_two.py`](bitwise/power_of_two.py) | 🟢 Easy |
| Count Set Bits | [Count 1s](https://www.geeksforgeeks.org/count-set-bits-in-an-integer/) | [`bitwise/count_bits.py`](bitwise/count_bits.py) | 🟡 Medium |
| XOR Operations | [XOR Properties](https://www.geeksforgeeks.org/xor-of-a-subarray-xor-queries/) | [`bitwise/xor_operations.py`](bitwise/xor_operations.py) | 🟡 Medium |

**Key Problems:** Single Number, Missing Number, Counting Bits

---

## 🚀 How to Use This Repository

### Prerequisites
- Python 3.7 or higher
- Basic understanding of programming concepts
- Familiarity with Python syntax

### Getting Started
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/dsa-python-roadmap.git
   cd dsa-python-roadmap
   ```

2. **Install dependencies (if any)**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start with basics**
   - Begin with Arrays and Strings
   - Read the theory links
   - Study the code implementations
   - Practice with the provided examples

4. **Practice methodology**
   - Understand the problem
   - Think of the approach
   - Implement the solution
   - Test with different inputs
   - Optimize if possible

### Study Plan

#### Beginner (4-6 weeks)
- Arrays, Strings, Linked Lists
- Basic Recursion, Stacks & Queues
- Simple Searching & Sorting

#### Intermediate (6-8 weeks)
- Hashing, Trees, Heaps
- Dynamic Programming basics
- Graph traversals (BFS, DFS)

#### Advanced (8-10 weeks)
- Advanced DP, Complex Graph algorithms
- Bit Manipulation, Advanced Trees
- System Design concepts

## 📝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### How to Contribute
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

If you have any questions or need help, please:
- Create an issue in this repository
- Reach out via email: [your-email@example.com]
- Connect on LinkedIn: [Your LinkedIn Profile]

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments

- [GeeksforGeeks](https://www.geeksforgeeks.org/) for comprehensive algorithm explanations
- [LeetCode](https://leetcode.com/) for practice problems
- [Python Documentation](https://docs.python.org/) for language reference
- The open-source community for inspiration and resources

---

**Happy Coding! 🎉**

*Remember: Consistency is key. Practice a little every day rather than cramming everything at once.*