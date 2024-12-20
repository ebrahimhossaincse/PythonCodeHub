import speedtest


def check_internet_speed():
    """
    Check internet speed (download, upload) and ISP information.
    """
    try:
        # Initialize the Speedtest class
        st = speedtest.Speedtest()

        # Get the best server
        st.get_best_server()
        print(f"ISP: {st.config['client']['isp']}")
        print(f"Country: {st.config['client']['country']}")

        # Measure download speed
        print("Measuring download speed...")
        download_speed = st.download() / 1_000_000  # Convert to Mbps

        # Measure upload speed
        print("Measuring upload speed...")
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps

        # Display results
        print(f"Download Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    check_internet_speed()
