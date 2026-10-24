import re
import tkinter as tk
from tkinter import ttk, messagebox
from ban_va_quyen import Nguoi


class ThanhVien(Nguoi):
    """Lớp dữ liệu Thành viên câu lạc bộ, kế thừa từ lớp Nguoi"""
    def __init__(self, ma_tv, ho_ten, so_dien_thoai, email="", ban_phu_trach="Truyền thông", diem_hoat_dong=0, trang_thai_hoi_phi=False):
        super().__init__(ho_ten, so_dien_thoai, email)
        self.ma_tv = ma_tv
        self.ban_phu_trach = ban_phu_trach
        self.__diem_hoat_dong = diem_hoat_dong if diem_hoat_dong >= 0 else 0
        self.trang_thai_hoi_phi = trang_thai_hoi_phi

    def get_diem_hoat_dong(self):
        return self.__diem_hoat_dong

    def set_diem_hoat_dong(self, diem_moi):
        if diem_moi >= 0:
            self.__diem_hoat_dong = diem_moi
            return True
        return False

    def cap_nhat_diem(self, diem_cong):
        if self.__diem_hoat_dong + diem_cong >= 0:
            self.__diem_hoat_dong += diem_cong
            return True
        return False

    def dong_hoi_phi(self):
        self.trang_thai_hoi_phi = True

    def hien_thi_thong_tin(self):
        tt_phi = "Đã đóng" if self.trang_thai_hoi_phi else "Chưa đóng"
        return (
            f"Mã TV: {self.ma_tv} | {super().hien_thi_thong_tin()} | "
            f"Ban: {self.ban_phu_trach} | Điểm: {self.__diem_hoat_dong} | Hội phí: {tt_phi}"
        )


class QuanLyThanhVien:
    """Lớp quản lý hồ sơ thành viên (CRUD, tìm kiếm, lọc và kiểm tra Regex)"""
    def __init__(self):
        self.danh_sach_tv = []

    def kiem_tra_regex(self, ma_tv, so_dien_thoai, email=""):
        mau_ma_tv = r"^TV\d{2,5}$"
        mau_sdt = r"^0[35789]\d{8}$"
        mau_email = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"

        if not re.match(mau_ma_tv, ma_tv):
            return False
        if not re.match(mau_sdt, so_dien_thoai):
            return False
        if email and not re.match(mau_email, email):
            return False
        return True

    def them_thanh_vien(self, tv_moi):
        if not self.kiem_tra_regex(tv_moi.ma_tv, tv_moi.so_dien_thoai, tv_moi.email):
            return False
        for tv in self.danh_sach_tv:
            if tv.ma_tv == tv_moi.ma_tv:
                return False
        self.danh_sach_tv.append(tv_moi)
        return True

    def doc_danh_sach(self):
        return self.danh_sach_tv

    def sua_thanh_vien(self, ma_tv, ho_ten_moi, sdt_moi, ban_moi):
        if not re.match(r"^0[35789]\d{8}$", sdt_moi):
            return False
        for tv in self.danh_sach_tv:
            if tv.ma_tv == ma_tv:
                tv.ho_ten = ho_ten_moi
                tv.so_dien_thoai = sdt_moi
                tv.ban_phu_trach = ban_moi
                return True
        return False

    def xoa_thanh_vien(self, ma_tv):
        for tv in self.danh_sach_tv:
            if tv.ma_tv == ma_tv:
                self.danh_sach_tv.remove(tv)
                return True
        return False

    def tim_kiem_thanh_vien(self, tu_khoa):
        tu_khoa = tu_khoa.lower().strip()
        return [
            tv for tv in self.danh_sach_tv
            if tu_khoa in tv.ma_tv.lower() or tu_khoa in tv.ho_ten.lower()
        ]

    def loc_theo_ban(self, ten_ban):
        if ten_ban == "Tất cả":
            return self.danh_sach_tv
        return [tv for tv in self.danh_sach_tv if tv.ban_phu_trach == ten_ban]


class CustomMemberCard(tk.Frame):
    """Lớp giao diện nâng cao hiển thị Thẻ thành viên CLB"""
    def __init__(self, parent, thanh_vien):
        super().__init__(parent, bd=2, relief="ridge", padx=12, pady=12, bg="white")
        self.thanh_vien = thanh_vien
        self.hien_thi_the()

    def hien_thi_the(self):
        tk.Label(
            self, text="THẺ THÀNH VIÊN CLB", font=("Arial", 11, "bold"),
            bg="#1e3a8a", fg="white", width=28, pady=5
        ).pack(pady=(0, 8))
        tk.Label(self, text=f"Mã TV: {self.thanh_vien.ma_tv}", bg="white", anchor="w").pack(fill="x")
        tk.Label(self, text=f"Họ tên: {self.thanh_vien.ho_ten}", bg="white", anchor="w").pack(fill="x")
        tk.Label(self, text=f"Ban: {self.thanh_vien.ban_phu_trach}", bg="white", anchor="w").pack(fill="x")
        tk.Label(self, text=f"Điểm HĐ: {self.thanh_vien.get_diem_hoat_dong()}", bg="white", anchor="w").pack(fill="x")


class GiaoDienQuanLyCLB(tk.Tk):
    """Lớp khung cửa sổ Tkinter chính (Menu, Notebook nhiều tab, Treeview)"""
    def __init__(self, quan_ly_tv=None):
        super().__init__()
        self.title("Ứng dụng Quản lý Câu lạc bộ Sinh viên - Nhóm 9")
        self.geometry("850x500")
        self.qltv = quan_ly_tv if quan_ly_tv is not None else QuanLyThanhVien()

        self.thiet_lap_menu()
        self.thiet_lap_notebook()
        self.thiet_lap_treeview()

    def thiet_lap_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        menu_he_thong = tk.Menu(menubar, tearoff=0)
        menu_he_thong.add_command(label="Thoát", command=self.quit)
        menubar.add_cascade(label="Hệ thống", menu=menu_he_thong)

    def thiet_lap_notebook(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=8, pady=8)

        self.tab_thanh_vien = ttk.Frame(self.notebook)
        self.tab_su_kien = ttk.Frame(self.notebook)
        self.tab_hoi_phi = ttk.Frame(self.notebook)
        self.tab_thong_ke = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_thanh_vien, text="Thành viên")
        self.notebook.add(self.tab_su_kien, text="Sự kiện")
        self.notebook.add(self.tab_hoi_phi, text="Hội phí")
        self.notebook.add(self.tab_thong_ke, text="Thống kê")

    def thiet_lap_treeview(self):
        cot = ("ma_tv", "ho_ten", "sdt", "ban", "diem")
        self.tree = ttk.Treeview(self.tab_thanh_vien, columns=cot, show="headings")
        self.tree.heading("ma_tv", text="Mã TV")
        self.tree.heading("ho_ten", text="Họ tên")
        self.tree.heading("sdt", text="Số điện thoại")
        self.tree.heading("ban", text="Ban phụ trách")
        self.tree.heading("diem", text="Điểm HĐ")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        for tv in self.qltv.doc_danh_sach():
            self.tree.insert("", "end", values=(
                tv.ma_tv, tv.ho_ten, tv.so_dien_thoai, tv.ban_phu_trach, tv.get_diem_hoat_dong()
            ))


# Chạy thử nghiệm các class trong file
if __name__ == "__main__":
    ql = QuanLyThanhVien()
    tv_1 = ThanhVien("TV001", "Vũ Hoàng Phúc", "0912345678", "phuc@gmail.com", "Truyền thông", 50)
    tv_1.cap_nhat_diem(10)
    tv_1.dong_hoi_phi()

    ql.them_thanh_vien(tv_1)
    print(tv_1.hien_thi_thong_tin())
    print("Số lượng thành viên hiện tại:", len(ql.doc_danh_sach()))