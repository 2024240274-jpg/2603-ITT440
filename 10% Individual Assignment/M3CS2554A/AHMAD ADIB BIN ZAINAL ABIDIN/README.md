# Digital Library Indexing System
NAME: AHMAD AIDB BIN ZAINAL ABIDIN

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
The system simulates a digital library consisting of multiple books. Each book contains a large number of randomly generated words, resulting in a dataset that reaches millions of total words. This approach mimics real-world large-scale text repositories without requiring external files.

Each book is processed to build a word-frequency index. The indexing process involves scanning the text and counting how many times each word appears. This type of indexing is fundamental in applications such as search engines and document analysis systems.

Three different execution approaches are applied to perform the same task:

- Sequential processing handles each book one at a time using a single CPU core.
  
- Concurrent processing introduces asynchronous operations and threading to allow partial overlap of tasks.
  
- Parallel processing uses multiprocessing to distribute the workload across multiple CPU cores, enabling simultaneous execution.
### The Algorithm
The indexing process is implemented using a simple counting mechanism. Each word in a book is analyzed and stored in a dictionary structure along with its frequency.


def index_text(book):
    name, content = book
    words = content.split()
    count = {}

    for w in words:
        count[w] = count.get(w, 0) + 1

    return name, count

This approach ensures that every word is processed and counted accurately, forming a basic but effective indexing system.

# Performance Result
The following results were captured by running the analyzer across three different paradigms:
| Method     | Time (s) |
| :--------- | :------- |
| Sequential | 2.1795s  |
| Concurrent | 2.0850s  |
| Parallel   | 1.0517s  |

Screenshot:
<img width="257" height="93" alt="image" src="https://github.com/user-attachments/assets/1ba4ed69-19f2-46c4-bf6c-af4453d3e8cf" />



# Patient Health Summary
The analyzer successfully processed the entire dataset with the following distribution:

  word 'index  ' : 999,008
  word 'data   ' : 1,000,224
  word 'memory ' : 999,409
  word 'python ' : 1,001,854
  word 'cpu    ' : 1,000,993
    

  Screenshot: 
<img width="571" height="256" alt="image" src="https://github.com/user-attachments/assets/42240895-cd7e-4101-9391-8c02f5130796" />


# Conclusion
The results highlight the importance of selecting an appropriate execution model for large-scale data processing tasks. For CPU-bound operations such as text indexing, multiprocessing provides a significant performance advantage over both sequential and threaded approaches.

This study reflects real-world scenarios in digital libraries and search systems, where efficient data processing directly impacts system responsiveness and scalability. The findings reinforce that parallel processing is essential for handling large datasets in modern computing environments.

# YouTube Demonstration
Link: [Demo Video](https://youtu.be/STmhzl5zYFo)
