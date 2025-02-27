from packages.bank import stats as bs, logic as b1, exports as be
from packages.crm import stats as cs, logic as c1, exports as ce

def main():
    bs.stat()
    b1.add(123)
    b1.change(321)
    b1.delete(453)
    b1.show()
    li = [1, 23, 4, 3, 3, 435, 34, 53]
    be.export(li)

    print("part 2")
    cs.stat()
    c1.add(123)
    c1.change(321)
    c1.delete(453)
    c1.show()
    li = [1, 23, 4, 3, 3, 435, 34, 53]
    ce.export(li)


if __name__ == "__main__":
    print("main.py was started")
    main()