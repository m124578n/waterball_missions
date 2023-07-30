from django_argparse_class import ArgparseTest


if __name__ == '__main__':
    print(__name__)
    a = ArgparseTest()
    print(a.prog_name)
    print(a.argv)