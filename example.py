from multiprocessing import Pool
from time import sleep
from tqdm import tqdm
import cloudpickle

# def f(x):
#     return x*x

def run_f(s):
    loads = s[0]
    f = loads(s[1])
    return f(s[2])

class myMath:
    def __init__(self, a):
        self.a = a

    def p_square(self):
        f = lambda a: a**2
        with Pool() as pool:
            # b = pool.imap(f, self.a)
            r = self.p_sq_in_parallel(pool,f)
            c = list(tqdm(iterable=r, desc="Collecting a**2 info", total=len(self.a)))
        return c
    
    def p_sq_in_parallel(self,pool,f):
        import cloudpickle
        s_f = cloudpickle.dumps(f)
        s_task = [(cloudpickle.loads, s_f, bs) for bs in self.a]
        r = pool.imap(run_f, s_task)
        return r



if __name__ == '__main__':
    ins = myMath([0,1,2,3,4,5,6,7,8,9,10])
    k = ins.p_square()
    print(k)
        # start 4 worker processes
    # f = lambda a : a**2

    # with Pool(processes=4) as pool:

    #     b = [0,1,2,3,4,5,6,7,8,9,10]
    #     import cloudpickle
    #     s_f = cloudpickle.dumps(f)
    #     s_task = [(cloudpickle.loads, s_f, bs) for bs in b]
    #     a = pool.imap(run_f, s_task)
    #     c = list(tqdm(iterable=a, desc="Collecting a**2 info", total=len(b)))
    #     print(c)
        # print same numbers in arbitrary order
        # for i in pool.imap_unordered(f, range(10)):
        #     print(i)

        # # evaluate "f(10)" asynchronously
        # res = pool.apply_async(f, [10])
        # print(res.get())             # prints "100"

        # # make worker sleep for 10 secs
        # res = pool.apply_async(sleep, [10])
        # print(res.get(timeout=5))             # raises multiprocessing.TimeoutError

    # exiting the 'with'-block has stopped the pool
