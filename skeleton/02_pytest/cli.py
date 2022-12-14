import argparse

def main():
    parser = argparse.ArgumentParser(prog='cli')
    parser.add_argument('--foo', help='the foo options!')
    parser.parse_args()
    parser.print_help()

if __name__ == '__main__':
    main()