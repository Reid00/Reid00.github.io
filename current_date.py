from datetime import datetime


def get_current_date():
    now = datetime.now().date()
    print(f'{now} \n')

if __name__ == '__main__':
    get_current_date()
