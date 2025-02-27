from package_bank import stats as bs, logic as b1, exports as be

def main():
    bs.stat()
    b1.add(123)
    b1.change(321)
    b1.delete(453)
    b1.show()
    li = [1, 23, 4, 3, 3, 435, 34, 53]
    be.export(li)


if __name__ == "__main__":
    print("main.py was started")
    main()
