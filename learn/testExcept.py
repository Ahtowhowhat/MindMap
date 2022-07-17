def f():
    try:
        return True
        raise Exception()
    except:
        # print(False)
        print('a')
        pass
    return False
print(f())