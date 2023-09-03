import datetime

def log_qr_code_generation(ip_address, qr_code_path):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] [IP: {ip_address}] [QR Code: {qr_code_path}]"
    
    with open('logs/qr_code_logs.txt', 'a') as file:
        file.write(f"{log_entry}\n")