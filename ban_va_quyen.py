class Nguoi:
    """Lớp cha cơ sở dùng để kế thừa"""
    def __init__(self, ho_ten, so_dien_thoai, email=""):
        self.ho_ten = ho_ten
        self.so_dien_thoai = so_dien_thoai
        self.email = email

    def hien_thi_thong_tin(self):
        return f"Họ tên: {self.ho_ten} | SĐT: {self.so_dien_thoai}"


class TaiKhoan:
    """Lớp quản lý tài khoản và phân quyền (Quản trị viên / Thành viên)"""
    def __init__(self, ten_dang_nhap, mat_khau, vai_tro="ThanhVien"):
        self.ten_dang_nhap = ten_dang_nhap
        self.__mat_khau = mat_khau  # Đóng gói mật khẩu, không hiển thị trực tiếp
        self.vai_tro = vai_tro

    def kiem_tra_mat_khau(self, mat_khau_nhap):
        return self.__mat_khau == mat_khau_nhap

    def doi_mat_khau(self, mat_khau_cu, mat_khau_moi):
        if self.kiem_tra_mat_khau(mat_khau_cu) and len(mat_khau_moi) >= 6:
            self.__mat_khau = mat_khau_moi
            return True
        return False


class BanPhuTrach:
    """Lớp dữ liệu Ban phụ trách trong CLB"""
    def __init__(self, ma_ban, ten_ban, truong_ban=""):
        self.ma_ban = ma_ban
        self.ten_ban = ten_ban
        self.truong_ban = truong_ban


class KhoanThuHoiPhi:
    """Lớp quản lý khoản thu hội phí của thành viên"""
    def __init__(self, ma_phieu, ma_tv, so_tien, ngay_thu, trang_thai=False):
        self.ma_phieu = ma_phieu
        self.ma_tv = ma_tv
        self.__so_tien = so_tien if so_tien >= 0 else 0
        self.ngay_thu = ngay_thu
        self.trang_thai = trang_thai

    def get_so_tien(self):
        return self.__so_tien

    def set_so_tien(self, so_tien_moi):
        if so_tien_moi >= 0:
            self.__so_tien = so_tien_moi
            return True
        return False

    def xac_nhan_dong_phi(self):
        self.trang_thai = True
        # Chạy thử nghiệm các class trong file
if __name__ == "__main__":
    nguoi_1 = Nguoi("Trần Nguyễn Như Ngọc", "0901234567")
    print(nguoi_1.hien_thi_thong_tin())

    tk_admin = TaiKhoan("nhungoc", "123456", "QuanTriVien")
    print("Kiểm tra mật khẩu:", tk_admin.kiem_tra_mat_khau("123456"))