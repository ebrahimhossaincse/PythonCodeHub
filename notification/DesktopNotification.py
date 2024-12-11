import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title='Md. Ebrahim Hossain',
            message="It's time to code",
            timeout=10,
        )
        time.sleep(10)