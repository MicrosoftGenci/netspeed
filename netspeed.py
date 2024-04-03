import speedtest
import time
import csv
from datetime import datetime


def test_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1024 / 1024  # Convert to Mbps
    upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps
    ping = st.results.ping  # Ping değeri

    return download_speed, upload_speed, ping


def save_to_csv(download_speed, upload_speed, ping, filename="internet_speed.csv"):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), download_speed, upload_speed,ping])


def main() -> object:
    test_interval = 60  # Her 1 dakikada bir test et
    while True:
        download_speed, upload_speed, ping = test_internet_speed()
        print(f"Tarih: {datetime.now()}")
        print(f"İndirme Hızı: {download_speed:.2f} Mbps")
        print(f"Yükleme Hızı: {upload_speed:.2f} Mbps")
        print(f"Ping: {ping} ms")
        print("-" * 50)

        save_to_csv(download_speed, upload_speed, ping)
        time.sleep(test_interval)


if __name__ == "__main__":
    main()