import logging

logging.basicConfig(filename='test.log', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')

def main():
    pass

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(e)
