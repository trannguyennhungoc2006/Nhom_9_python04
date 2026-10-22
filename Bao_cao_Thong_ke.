import random

class ThongKeHoatDong:
    def __init__(self, ds_thanh_vien=None, ds_su_kien=None):
        self.__ds_thanh_vien = ds_thanh_vien if ds_thanh_vien is not None else []
        self.__ds_su_kien = ds_su_kien if ds_su_kien is not None else []

    def get_ds_thanh_vien(self):
        return self.__ds_thanh_vien

    def set_ds_thanh_vien(self, ds_moi):
        if isinstance(ds_moi, list):
            self.__ds_thanh_vien = ds_moi
            return True
        return False

    def get_ds_su_kien(self):
        return self.__ds_su_kien

    def set_ds_su_kien(self, ds_moi):
        if isinstance(ds_moi, list):
            self.__ds_su_kien = ds_moi
            return True
        return False

    def sinh_du_lieu_mau(self, so_luong=5):
        if so_luong > 0:
            self.__ds_thanh_vien = [f"TV{i}" for i in range(1, so_luong + 1)]
            self.__ds_su_kien = [random.randint(10, 50) for _ in range(so_luong)]
            return True
        return False

    def thong_ke_thanh_vien_tich_cuc(self):
        return self.__ds_thanh_vien

    def thong_ke_su_kien_dong_nguoi(self):
        return self.__ds_su_kien

    def ve_bieu_do_canvas(self, canvas):
        return canvas is not None

    def xuat_bao_cao_csv(self, ten_file):
        return ten_file.endswith(".csv")

    def xuat_bao_cao_json(self, ten_file):
        return ten_file.endswith(".json")

if __name__ == "__main__":
    tk_hd = ThongKeHoatDong()
    tk_hd.sinh_du_lieu_mau(3)
    print("Danh sách thành viên mẫu:", tk_hd.get_ds_thanh_vien())
    print("Kiểm tra xuất file CSV:", tk_hd.xuat_bao_cao_csv("bao_cao.csv"))
