import time
import asyncio
import threading
import random
from multiprocessing import Pool

# -------------------------------
# SETTINGS
# -------------------------------
NUM_BOOKS = 20
WORDS_PER_BOOK = 500000  # 20 × 500,000 = 10,000,000 words

WORDS = ["python", "data", "library", "index", "search",
         "thread", "process", "async", "cpu", "memory"]


# -------------------------------
# THREADING (LOGGING)
# -------------------------------
def log_message(msg):
    print("[LOG]", msg)

def threaded_logger(messages):
    threads = []
    for m in messages:
        t = threading.Thread(target=log_message, args=(m,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


# -------------------------------
# GENERATE DATA
# -------------------------------
def generate_books():
    books = []
    for i in range(NUM_BOOKS):
        words = []
        for _ in range(WORDS_PER_BOOK):
            words.append(random.choice(WORDS))
        text = " ".join(words)
        books.append(("Book_" + str(i+1), text))
    return books


# -------------------------------
# ASYNC (SIMULATE READING)
# -------------------------------
async def read_book(book):
    return book

async def read_all(books):
    tasks = []
    for b in books:
        tasks.append(read_book(b))
    return await asyncio.gather(*tasks)


# -------------------------------
# INDEXING
# -------------------------------
def index_text(book):
    name, content = book
    words = content.split()
    count = {}

    for w in words:
        count[w] = count.get(w, 0) + 1

    return name, count


# -------------------------------
# THREE METHODS
# -------------------------------
def run_sequential(books):
    start = time.time()

    results = []
    for b in books:
        results.append(index_text(b))

    return results, time.time() - start


def run_concurrent(books):
    start = time.time()

    def background():
        time.sleep(0.05)

    t = threading.Thread(target=background)
    t.start()

    contents = asyncio.run(read_all(books))

    results = []
    for b in contents:
        results.append(index_text(b))

    t.join()

    return results, time.time() - start


def run_parallel(books):
    start = time.time()

    contents = asyncio.run(read_all(books))

    with Pool() as p:
        results = p.map(index_text, contents)

    return results, time.time() - start


# -------------------------------
# SUMMARY 
# -------------------------------
def show_summary(seq, con, par):
    res, t1 = seq
    _, t2 = con
    _, t3 = par

    # Combine all book indexes into one
    total_index = {}

    for _, index in res:
        for word, count in index.items():
            total_index[word] = total_index.get(word, 0) + count

    print("\n" + "="*55)
    print("              LIBRARY INDEX SUMMARY")
    print("="*55)

    # Show 5 sample words (like your image)
    sample_words = list(total_index.items())[:5]

    for word, count in sample_words:
        print(f"Word '{word:<10}' : {count:,}")

    print("-" * 55)
    print(f"Total Books : {NUM_BOOKS}")
    print(f"Total Words : {NUM_BOOKS * WORDS_PER_BOOK:,}")
    print("="*55)

    # Timing (extra, but useful)
    print("\nExecution Time:")
    print(f"Sequential : {t1:.4f}s")
    print(f"Concurrent : {t2:.4f}s")
    print(f"Parallel   : {t3:.4f}s")


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    print("Generating 10 million words dataset...")
    books = generate_books()

    threaded_logger([
        "Starting Sequential...",
        "Starting Concurrent...",
        "Starting Parallel..."
    ])

    s = run_sequential(books)
    c = run_concurrent(books)
    p = run_parallel(books)

    show_summary(s, c, p)