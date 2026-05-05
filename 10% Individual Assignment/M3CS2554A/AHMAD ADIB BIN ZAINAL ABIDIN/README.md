# Parallel Digital Library Indexing System
NAME: AHMAD ADIB BIN ZAINAL ABIDIN

STUDENT ID: 2024240274

# Introduction
In large-scale digital platforms such as online libraries, search engines, and document repositories, the ability to process and index massive volumes of text data efficiently is essential. These systems must handle millions of words across multiple documents while maintaining fast response times for search and retrieval.

This project focuses on the computational efficiency of indexing a dataset containing millions of words distributed across multiple digital books. The system analyzes the text and generates word-frequency indexes, which are commonly used in search engines and information retrieval systems.

The main objective is to evaluate how different execution models—Sequential, Concurrent, and Parallel—utilize system resources and affect performance, particularly when handling large datasets on multi-core consumer hardware.

# System
## Demonstration System

Operating System: Windows 11

Python Version: 3.14

CPU Cores: 12 cores

RAM: 16GB DDR4

## User Manual

### 1. System Requirements
Operating System: Windows 10/11

Language: Python 3.8 or higher

Hardware: Minimum 4GB RAM (8GB+ recommended for 10 million records)

Libraries: Standard Python libraries (`random`, `time`, `threading`, `multiprocessing`)

### 2. Installation Steps
1.  **Install Python**: Download and install the latest version of Python from [python.org](https://www.python.org/).
2.  **Download the Project**:
    *   Clone this repository or download the `python digital_library.py` file directly to your computer.
3.  **Setup Environment**: No external libraries are required as the project uses built-in Python modules.

### 3. How to Run the Program
1.  Open your **Command Prompt (CMD)** or **Terminal**.
2.  Navigate to the folder where you saved the file.
3.  Run the program using the following command:
    ```bash
    python digital_library.py
    ```

# Objectives
1. To implement a scalable digital library indexing system capable of handling millions of words.

2. To evaluate the performance differences between sequential, concurrent, and parallel processing models.

3. To analyze the impact of Python’s execution model on CPU-bound workloads.

4. To generate a word-frequency index that can support fast search operations in large text datasets.

# Methodology
The system generates a dataset consisting of 20 books. Each book contains 500,000 randomly selected words from a predefined list. This results in a total of 10,000,000 words.

Each book is processed using an indexing function that counts the frequency of each word. This simulates a real-world indexing system used in search engines.

Three execution methods are implemented.

The Sequential method processes books one by one.

The Concurrent method uses threading and asynchronous execution to simulate overlapping tasks.

The Parallel method uses multiprocessing to distribute the workload across multiple CPU cores.
### The Algorithm
The system processes a large-scale digital library dataset by performing word indexing on each generated book. Each book consists of randomly generated words, and the goal is to count how many times each word appears.
Indexing Logic

The main function responsible for this process is index_text. It takes a single book as input and produces a word frequency index.

def index_text(book):
    name, content = book
    words = content.split()
    count = {}

    for w in words:
        count[w] = count.get(w, 0) + 1

    return name, count
# Performance Result
The following results were captured by running the analyzer across three different paradigms:
| Method     | Time (s) |
| :--------- | :------- |
| Sequential |  1.1420s |
| concurrent |  1.1504s |
| Parallel   |  0.9091s |

Screenshot:
<img width="408" height="145" alt="image" src="https://github.com/user-attachments/assets/9bfa60f0-3ace-4caa-b2bf-11e9e68825ac" />




# Library Index Summary
The analyzer successfully processed the entire dataset with the following distribution:

word 'memory' : 999,821
word 'async'  : 999,405
word 'index'  : 999,886
word 'search' : 999,642
word ' data'  : 999,155

total books   : 20
total words   : 10,000,000

  Screenshot: 
<img width="927" height="420" alt="image" src="https://github.com/user-attachments/assets/f845e6a4-7c5a-46ef-b3fd-f668d197dd13" />


# Conclusion
This project demonstrates that for CPU-bound tasks such as text indexing, multiprocessing can provide performance benefits when used correctly. However, it also highlights that parallel processing introduces overhead that can reduce efficiency if the workload is not properly balanced.

Sequential execution remains the most straightforward approach, while concurrent execution is more suitable for I/O-bound tasks. Parallel processing is powerful but must be carefully designed to achieve optimal results.

# YouTube Demonstration
Link: [Demo Video](https://youtu.be/STmhzl5zYFo)
