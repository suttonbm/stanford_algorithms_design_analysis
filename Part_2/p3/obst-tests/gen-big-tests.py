from random import randint

def main():
    for k in range(1,3):
        with open('test{0}.txt'.format(k*10),'w') as testfile:
            testfile.write('{0} '.format(k*1000))
            for j in range(k*1000):
                testfile.write('{0} '.format(randint(1, 1000)))
            # END for
        # END with
    # END for

if __name__ == '__main__':
    main()
