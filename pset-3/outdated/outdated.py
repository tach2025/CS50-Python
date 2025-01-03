month_name = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
        middle_endian_date = input("Date: ").strip()
        if '/' in middle_endian_date:
            m, d, y = middle_endian_date.split('/')
            m = int(m)
            d = int(d)
            y = int(y)
            if m < 1 or m > 12:
                raise Exception
            if d < 1 or d > 31:
                raise Exception
            print(f"{y:04}-{m:02}-{d:02}")
        else:
            m_d, y = middle_endian_date.split(',')
            y = int(y)
            m_name, d = m_d.split()
            d = int(d)
            m = month_name.index(m_name.title()) + 1
            if m < 1 or m > 12:
                raise Exception
            if d < 1 or d > 31:
                raise Exception
            print(f"{y:04}-{m:02}-{d:02}")
    except:
        continue
    else:
        break
