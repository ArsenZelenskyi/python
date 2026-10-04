import re

def read_chunks(filename, chunk_size = 4096):
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk


def check_lines(filename):
    check_pat = re.compile(r'"\s+(\d{3})\s+(\d+|-)')
    for line in filename:
        r_bytes = (
            len(line.encode("utf-8")) if isinstance(line,str) else len(line)
        )
        line_str = (
            line if isinstance(line,str) else line.decode("utf-8", errors="ignore")
        )
        match = check_pat.search(line_str)
        if match:
            send = match.group(2)
            b_send = int(send) if send.isdigit() else 0
        else:
            b_send = 0
        yield r_bytes, b_send


def calc_total_bytes(filename):
    total_bytes = 0
    total_send_bytes = 0
    with open(filename, 'r', encoding= "utf-8", errors="ignore") as f:
        for rec,send in check_lines(f):
            total_bytes += rec
            total_send_bytes += send

    return total_bytes, total_send_bytes


def main():
    file_name = "2017_05_07_nginx.txt"
    try:
        rec, send = calc_total_bytes(file_name)
        print(f"Прийнято {rec} байтів")
        print(f"Відправлено {send} байтів")
    except FileNotFoundError:
        print("Файл не знайдено")


if __name__ == "__main__":
    main()