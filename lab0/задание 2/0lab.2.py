import time

start_time = time.perf_counter()
with open("input2.txt")as f:
    n = int(f.read())
def calc_fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b
if 0 <=n<= 45:
    res = calc_fib(n)
    print(res)
    with open("output2.txt", "a+") as f:
        f.write(str(res) + "\n")
end_time = time.perf_counter()
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time} ms")