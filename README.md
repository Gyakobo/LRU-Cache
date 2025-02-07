# LRU (Least Recently Used) Cache  

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white)

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

## Introduction

This project utilizes and showcases how an LRU Cache operates. An **LRU (Least Recently Used)** Cache is a data structure that stores a limited number of items and removes the leaset recently used item when the cache reaches its capacity. This ensures that frequently accessed items remain in the cache while older, less accessed items are evicted.

## History 

The **Least Recently Used (LRU) Cache** was formally described in research papers in the 1960s and 1970s as an efficient cache eviction policy. It became widely used in computer architecture, operating systems, and database management. The concept was integral to early virtual memory management systems, CPU cache design, and page replacement algorithms.

## Methodology

The LRU caching mechanism follows these principles:

1. `Capacity Restriction`: It stores a fixed number of key-value pairs.

2. `Recency Tracking`: When an item is accessed, it is moved to the most recently used position.

3. `Eviction Policy`: When the cache is full, the least recently used item is removed.

### Data Structures Used 

An efficient LRU cache is typically implemented using:

* `Hash Map (Dictionary in Python)`: To store key-value pairs for O(1) access time.

* `Doubly Linked List`: To maintain the order of usage, enabling efficient insertions and deletions.

### Complexity Analysis

* `Insertion (put) and Lookup (get)`: O(1) using an OrderedDict (doubly linked list + hashmap).

* `Eviction`: O(1) as the least recently used item is efficiently removed.

### Applications
 
* `Operating Systems`: Page replacement algorithms in memory management.

* `Web Browsers`: Caching recently visited pages.

* `Databases`: Buffer management in database management systems.

* `Distributed Systems`: Caching frequently requested data to reduce latency.

## Alternate Caching Policies

* `FIFO (First-In-First-Out)`: Evicts the oldest item first.

* `LFU (Least Frequently Used)`: Removes the least accessed item over time.

* `MRU (Most Recently Used)`: Opposite of LRU; removes the most recently used item.

## Conclusion 

LRU Cache is a powerfule and widely used caching strategy optimized for fast access and efficient memory utilization. Its implementation combines a hash map and a doubly linked list to achieve O(1) time complexity for both get and put operations.

## License
MIT



