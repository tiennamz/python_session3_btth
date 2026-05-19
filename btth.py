while True:
    choice = int(input("Nhập số lượng nhân viên: "))
    
    for i in range(choice):
        print(f"Nhân viên {i+1}")
        name = input("Tên nhân viên: ")
        date = int(input("Số ngày đi làm: "))
        print("Thông tin nhân viên")
        print(f"Tên: {name}")
        print(f"Số ngày đi làm: {date}")
        if date > 20:
            print("Nhân viên chuyên cần tốt")
        else:
            print("Cần cải thiện chuyên cần")
        
    while True:
        again_choice = input("Tiếp tục chương trình? (y/n) ")
        match again_choice:
            case "y":
                print("\n")
                break
            case "n":
                print("Chương trình kết thúc")
                break
            case _:
                print("Lỗi cú pháp")
        
        
    break
        
        
        
        
