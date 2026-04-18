import random

def get_random_dsa_question():
    # A curated list of common DSA practice questions
    dsa_questions = [
        "Given an array of integers, find two numbers such that they add up to a specific target number.",
        "Implement a function to reverse a singly linked list.",
        "Check if a given binary tree is a valid Binary Search Tree (BST).",
        "Find the longest substring without repeating characters in a given string.",
        "Implement Depth First Search (DFS) on a graph represented as an adjacency list.",
        "Find the median of two sorted arrays of different sizes.",
        "Determine if a linked list has a cycle.",
        "Find the shortest path in an unweighted graph using Breadth First Search (BFS).",
        "Implement a stack using two queues.",
        "Given an array, find the next greater element for every element."
    ]
    
    question = random.choice(dsa_questions)
    return question

if __name__ == "__main__":
    print("--- Daily DSA Challenge ---")
    print(f"Your question is: {get_random_dsa_question()}")
