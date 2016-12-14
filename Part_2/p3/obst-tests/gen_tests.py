from random import randint

def main():
    for k in range(10):
        with open('test{0}.txt'.format(k),'w') as testfile:
            testfile.write('{0} '.format(k*10))
            for j in range(k*10):
                testfile.write('{0} '.format(randint(1, 100)))
            # END for
        # END with
    # END for

if __name__ == '__main__':
    main()
