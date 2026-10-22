class SuKien:
    """Lớp dữ liệu Sự kiện của câu lạc bộ"""
    def __init__(self, ma_sk, ten_sk, ngay_to_chuc, dia_diem, diem_thuong=5):
        self.ma_sk = ma_sk
        self.ten_sk = ten_sk
        self.ngay_to_chuc = ngay_to_chuc
        self.dia_diem = dia_diem
        self.__diem_thuong = diem_thuong if diem_thuong > 0 else 0

    def get_diem_thuong(self):
        return self.__diem_thuong

    def set_diem_thuong(self, diem_moi):
        if diem_moi > 0:
            self.__diem_thuong = diem_moi
            return True
        return False


class DangKySuKien:
    """Lớp ghi nhận đăng ký và điểm danh sự kiện"""
    def __init__(self, ma_sk, ma_tv, trang_thai_dang_ky=True, trang_thai_diem_danh="Vắng"):
        self.ma_sk = ma_sk
        self.ma_tv = ma_tv
        self.trang_thai_dang_ky = trang_thai_dang_ky
        self.trang_thai_diem_danh = trang_thai_diem_danh

    def diem_danh_co_mat(self):
        self.trang_thai_diem_danh = "Có mặt"


class QuanLySuKien:
    """Lớp quản lý nghiệp vụ sự kiện và điểm danh"""
    def __init__(self):
        self.danh_sach_sk = []
        self.danh_sach_dang_ky = []

    def tao_su_kien(self, su_kien_moi):
        for sk in self.danh_sach_sk:
            if sk.ma_sk == su_kien_moi.ma_sk:
                return False
        self.danh_sach_sk.append(su_kien_moi)
        return True

    def dang_ky_tham_gia(self, ma_sk, ma_tv):
        ban_ghi = DangKySuKien(ma_sk, ma_tv)
        self.danh_sach_dang_ky.append(ban_ghi)
        return ban_ghi