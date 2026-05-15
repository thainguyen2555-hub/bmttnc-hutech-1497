from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while True:
    print('\nCHUONG TRINH QUAN LY SINH VIEN')
    print('****************MENU****************')
    print('**  1. Them sinh vien.            **')
    print('**  2. Cap nhat thong tin sinh vien boi ID. **')
    print('**  3. Xoa sinh vien boi ID.      **')
    print('**  4. Tim kiem sinh vien theo ten. **')
    print('**  5. Sap xep sinh vien theo diem trung binh. **')
    print('**  6. Sap xep sinh vien theo ten. **')
    print('**  7. Hien thi danh sach sinh vien. **')
    print('**  8. Thoat                      **')
    print('************************************')

    key = int(input('Nhap tuy chon: '))
    if (key == 1):
        qlsv.nhapSinhVien()
        print('\nThem sinh vien thanh cong!')

    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            ID = int(input("Nhap ID: "))
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sach sinh vien trong!")

    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            ID = int(input("Nhap ID: "))
            if (qlsv.deleteById(ID)):
                print(f"\nSinh vien co id = {ID} da bi xoa.")
            else:
                print(f"\nSinh vien co id = {ID} khong ton tai.")
        else:
            print("\nDanh sach sinh vien trong!")

    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            name = input("Nhap ten de tim kiem: ")
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien trong!")

    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")

    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")

    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")

    elif (key == 8):
        print("\nBan da chon thoat chuong trinh!")
        break

    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")
