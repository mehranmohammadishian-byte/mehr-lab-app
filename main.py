# -*- coding: utf-8 -*-
# Mehr Pathobiology Laboratory - Main Application
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem, MDList
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivy.uix.scrollview import ScrollView
from kivy.core.text import LabelBase
import data
import converter
import audit_data
import math
import datetime
import os
import arabic_reshaper
from bidi.algorithm import get_display

# وارد کردن کلاس‌های پایه برای ارث‌بری
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton

Window.size = (420, 760)
Window.minimum_width = 360
Window.minimum_height = 600

# --- Register Persian Font for Kivy ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(BASE_DIR, "Vazirmatn-Regular.ttf")
try:
    LabelBase.register(name="Vazir", fn_regular=FONT_PATH)
except Exception as e:
    print(f"Kivy Font registration failed: {e}")

# --- Register Persian Font for ReportLab (PDF) ---
try:
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    pdfmetrics.registerFont(TTFont('Vazir', FONT_PATH))
except Exception as e:
    print(f"ReportLab Font registration failed: {e}")

# --- ایجاد کلاس‌های سفارشی برای تحمیل فونت فارسی در KivyMD ---
class PersianMDLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = "Vazir"

class PersianMDRaisedButton(MDRaisedButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = "Vazir"

KV = """
ScreenManager:
    id: screen_manager
    MDScreen:
        name: "login"
        MDBoxLayout:
            orientation: "vertical"
            padding: "40dp"
            spacing: "20dp"
            Widget:
            MDIcon:
                icon: "microscope"
                halign: "center"
                font_size: "80sp"
                theme_text_color: "Custom"
                text_color: 0.0, 0.75, 0.75, 1
                size_hint_y: None
                height: "100dp"
            MDLabel:
                text: "Mehr Pathobiology Laboratory"
                halign: "center"
                font_style: "H5"
                size_hint_y: None
                height: "40dp"
            MDLabel:
                text: "Prepared by: Mehran Mohammadi"
                halign: "center"
                font_style: "Caption"
                size_hint_y: None
                height: "24dp"
            Widget:
                size_hint_y: None
                height: "20dp"
            MDTextField:
                id: login_password
                hint_text: "Enter Password"
                mode: "rectangle"
                password: True
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
            MDRaisedButton:
                text: "LOGIN"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.6
                on_release: app.verify_login()
            Widget:
    MDScreen:
        name: "menu"
        MDBoxLayout:
            orientation: "vertical"
            padding: "20dp"
            spacing: "16dp"
            MDIcon:
                icon: "microscope"
                halign: "center"
                font_size: "64sp"
                theme_text_color: "Custom"
                text_color: 0.0, 0.75, 0.75, 1
                size_hint_y: None
                height: "70dp"
            MDLabel:
                text: "Mehr Pathobiology Laboratory"
                halign: "center"
                font_style: "H4"
                size_hint_y: None
                height: "50dp"
            MDLabel:
                text: "Prepared by: Mehran Mohammadi"
                halign: "center"
                font_style: "Caption"
                size_hint_y: None
                height: "24dp"
            MDLabel:
                text: "Laboratory Reference and Unit Converter"
                halign: "center"
                size_hint_y: None
                height: "40dp"
            MDRaisedButton:
                text: "Search Tests"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.9
                on_release: app.go_to("search")
            MDRaisedButton:
                text: "All Tests"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.9
                on_release: app.go_to("tests")
            MDRaisedButton:
                text: "Critical Value Check"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.9
                on_release: app.go_to("critical")
            MDRaisedButton:
                text: "Unit Converter"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.9
                on_release: app.go_to("converter")
            MDRaisedButton:
                text: "Date Converter"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.9
                on_release: app.go_to("date_converter")
            MDRaisedButton:
                text: "QC Statistics"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.9
                on_release: app.go_to("qc")
            MDRaisedButton:
                text: "Internal Audit"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.9
                on_release: app.go_to("audit")
            Widget:
    MDScreen:
        name: "search"
        MDBoxLayout:
            orientation: "vertical"
            padding: "12dp"
            spacing: "8dp"
            MDBoxLayout:
                adaptive_height: True
                MDIconButton:
                    icon: "arrow-left"
                    on_release: app.go_to("menu")
                MDLabel:
                    text: "Search Tests"
                    font_style: "H5"
            MDTextField:
                id: search_input
                hint_text: "Enter test name or category"
                mode: "rectangle"
                on_text: app.search_tests_live(self.text)
            ScrollView:
                MDBoxLayout:
                    id: search_results
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: "4dp"
    MDScreen:
        name: "tests"
        MDBoxLayout:
            orientation: "vertical"
            padding: "12dp"
            spacing: "8dp"
            MDBoxLayout:
                adaptive_height: True
                MDIconButton:
                    icon: "arrow-left"
                    on_release: app.go_to("menu")
                MDLabel:
                    text: "All Tests"
                    font_style: "H5"
            MDTextField:
                id: all_tests_search
                hint_text: "Filter by test or category"
                mode: "rectangle"
                on_text: app.filter_all_tests(self.text)
            ScrollView:
                MDBoxLayout:
                    id: all_tests_list
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: "4dp"
    MDScreen:
        name: "detail"
        MDBoxLayout:
            orientation: "vertical"
            padding: "16dp"
            spacing: "12dp"
            MDBoxLayout:
                adaptive_height: True
                MDIconButton:
                    icon: "arrow-left"
                    on_release: app.go_back_from_detail()
                MDLabel:
                    text: "Test Details"
                    font_style: "H5"
            MDLabel:
                id: detail_name
                text: ""
                font_style: "H6"
                adaptive_height: True
            ScrollView:
                MDLabel:
                    id: detail_info
                    text: ""
                    size_hint_y: None
                    height: max(self.texture_size[1], dp(40))
                    text_size: self.width, None
                    halign: "left"
                    valign: "top"
                    padding: dp(4), dp(4)
    MDScreen:
        name: "critical"
        MDBoxLayout:
            orientation: "vertical"
            padding: "16dp"
            spacing: "12dp"
            MDBoxLayout:
                adaptive_height: True
                MDIconButton:
                    icon: "arrow-left"
                    on_release: app.go_to("menu")
                MDLabel:
                    text: "Critical Value Check"
                    font_style: "H5"
            MDRaisedButton:
                id: crit_test_btn
                text: "Select Test"
                size_hint_x: 1
                on_release: app.open_critical_test_picker()
            MDTextField:
                id: crit_value
                hint_text: "Numeric result"
                mode: "rectangle"
                input_filter: "float"
            MDRaisedButton:
                text: "Check Result"
                pos_hint: {"center_x": 0.5}
                on_release: app.check_critical_live()
            MDLabel:
                id: crit_result
                text: ""
                halign: "center"
                adaptive_height: True
                font_style: "H6"
                theme_text_color: "Custom"
                text_color: 0.9, 0.9, 0.9, 1
            MDLabel:
                text: "Use the unit and critical limits configured by your laboratory."
                adaptive_height: True
                font_style: "Caption"
    MDScreen:
        name: "converter"
        MDBoxLayout:
            orientation: "vertical"
            padding: "16dp"
            spacing: "12dp"
            MDBoxLayout:
                adaptive_height: True
                MDIconButton:
                    icon: "arrow-left"
                    on_release: app.go_to("menu")
                MDLabel:
                    text: "Unit Converter"
                    font_style: "H5"
            MDTextField:
                id: conv_value
                hint_text: "Enter value"
                mode: "rectangle"
                input_filter: "float"
            MDRaisedButton:
                id: conv_analyte
                text: "Analyte: Select"
                size_hint_x: 1
                on_release: app.open_unit_menu("analyte")
            MDBoxLayout:
                adaptive_height: True
                spacing: "8dp"
                MDRaisedButton:
                    id: conv_from
                    text: "From Unit"
                    size_hint_x: 0.5
                    on_release: app.open_unit_menu("from")
                MDRaisedButton:
                    id: conv_to
                    text: "To Unit"
                    size_hint_x: 0.5
                    on_release: app.open_unit_menu("to")
            MDRaisedButton:
                text: "Convert"
                pos_hint: {"center_x": 0.5}
                on_release: app.do_convert()
            MDLabel:
                id: conv_result
                text: ""
                halign: "center"
                adaptive_height: True
                font_style: "H6"
                theme_text_color: "Custom"
                text_color: 0.9, 0.9, 0.9, 1
            MDLabel:
                text: "Supported conversion pairs"
                font_style: "Subtitle1"
                adaptive_height: True
            ScrollView:
                MDBoxLayout:
                    id: conv_list
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: "4dp"
    # ==================== DATE CONVERTER SCREEN ====================
    MDScreen:
        name: "date_converter"
        MDBoxLayout:
            orientation: "vertical"
            padding: "16dp"
            spacing: "12dp"
            MDBoxLayout:
                adaptive_height: True
                MDIconButton:
                    icon: "arrow-left"
                    on_release: app.go_to("menu")
                MDLabel:
                    text: "Date Converter"
                    font_style: "H5"
            ScrollView:
                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: "12dp"
                    MDLabel:
                        text: "Enter Date:"
                        font_style: "Subtitle1"
                        adaptive_height: True
                    MDBoxLayout:
                        adaptive_height: True
                        spacing: "8dp"
                        MDTextField:
                            id: date_year
                            hint_text: "Year"
                            mode: "rectangle"
                            input_filter: "int"
                            size_hint_x: 0.5
                        MDRaisedButton:
                            id: date_month_btn
                            text: "Month"
                            size_hint_x: 0.5
                            on_release: app.open_date_month_menu()
                        MDTextField:
                            id: date_day
                            hint_text: "Day"
                            mode: "rectangle"
                            input_filter: "int"
                            size_hint_x: 1
                    MDLabel:
                        text: "From Calendar:"
                        font_style: "Caption"
                        adaptive_height: True
                    MDRaisedButton:
                        id: date_from_btn
                        text: "Jalali (Shamsi)"
                        size_hint_x: 1
                        on_release: app.open_date_from_menu()
                    MDLabel:
                        text: "To Calendar:"
                        font_style: "Caption"
                        adaptive_height: True
                    MDRaisedButton:
                        id: date_to_btn
                        text: "Gregorian (Miladi)"
                        size_hint_x: 1
                        on_release: app.open_date_to_menu()
                    MDRaisedButton:
                        text: "Convert Date"
                        pos_hint: {"center_x": 0.5}
                        on_release: app.do_date_convert()
                    MDLabel:
                        id: date_result
                        text: ""
                        halign: "center"
                        adaptive_height: True
                        font_style: "H6"
                        theme_text_color: "Custom"
                        text_color: 0.9, 0.9, 0.9, 1
                    Widget:
                        size_hint_y: None
                        height: "20dp"
    MDScreen:
        name: "qc"
        MDBoxLayout:
            orientation: "vertical"
            padding: "12dp"
            spacing: "8dp"
            MDBoxLayout:
                adaptive_height: True
                MDIconButton:
                    icon: "arrow-left"
                    on_release: app.go_to("menu")
                MDLabel:
                    text: "QC Statistics"
                    font_style: "H5"
            ScrollView:
                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: "12dp"
                    MDLabel:
                        text: "Statistics (Mean / SD / CV%)"
                        font_style: "Subtitle1"
                        adaptive_height: True
                    MDLabel:
                        text: "Paste values (comma, space, or newline):"
                        font_style: "Caption"
                        adaptive_height: True
                    MDTextField:
                        id: qc_data1
                        hint_text: "e.g. 98, 102, 99, 101 ..."
                        mode: "rectangle"
                        multiline: True
                        size_hint_y: None
                        height: "110dp"
                    MDRaisedButton:
                        text: "Calculate Stats"
                        pos_hint: {"center_x": 0.5}
                        on_release: app.calculate_qc_stats()
                    MDBoxLayout:
                        adaptive_height: True
                        spacing: "8dp"
                        MDTextField:
                            id: qc_mean
                            hint_text: "Mean"
                            mode: "rectangle"
                            readonly: True
                            size_hint_x: 0.33
                        MDTextField:
                            id: qc_sd
                            hint_text: "SD"
                            mode: "rectangle"
                            readonly: True
                            size_hint_x: 0.33
                        MDTextField:
                            id: qc_cv
                            hint_text: "CV%"
                            mode: "rectangle"
                            readonly: True
                            size_hint_x: 0.33
                    MDLabel:
                        text: "———————————————"
                        adaptive_height: True
                        halign: "center"
                    MDLabel:
                        text: "Comparison (Regression / F-test)"
                        font_style: "Subtitle1"
                        adaptive_height: True
                    MDLabel:
                        text: "Data Set 1 (X):"
                        font_style: "Caption"
                        adaptive_height: True
                    MDTextField:
                        id: qc_x
                        hint_text: "e.g. 10, 20, 30 ..."
                        mode: "rectangle"
                        multiline: True
                        size_hint_y: None
                        height: "90dp"
                    MDLabel:
                        text: "Data Set 2 (Y):"
                        font_style: "Caption"
                        adaptive_height: True
                    MDTextField:
                        id: qc_y
                        hint_text: "e.g. 11, 21, 31 ..."
                        mode: "rectangle"
                        multiline: True
                        size_hint_y: None
                        height: "90dp"
                    MDRaisedButton:
                        text: "Compare"
                        pos_hint: {"center_x": 0.5}
                        on_release: app.open_qc_compare_menu()
                    MDLabel:
                        id: qc_compare_result
                        text: ""
                        adaptive_height: True
                        halign: "center"
                        font_style: "Caption"
                        theme_text_color: "Custom"
                        text_color: 0.9, 0.9, 0.9, 1
                    MDRaisedButton:
                        text: "Generate PDF Report"
                        pos_hint: {"center_x": 0.5}
                        on_release: app.generate_qc_pdf()
                    Widget:
                        size_hint_y: None
                        height: "20dp"
    MDScreen:
        name: "audit"
        MDBoxLayout:
            orientation: "vertical"
            padding: "16dp"
            spacing: "12dp"
            MDBoxLayout:
                adaptive_height: True
                MDIconButton:
                    icon: "arrow-left"
                    on_release: app.go_to("menu")
                MDLabel:
                    text: "Internal Audit"
                    font_style: "H5"
            ScrollView:
                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: "10dp"
                    MDLabel:
                        text: "Language / Zaban:"
                        font_style: "Subtitle1"
                        adaptive_height: True
                    MDBoxLayout:
                        adaptive_height: True
                        spacing: "8dp"
                        MDRaisedButton:
                            id: lang_en_btn
                            text: "English"
                            size_hint_x: 0.5
                            on_release: app.set_audit_language("en")
                        MDRaisedButton:
                            id: lang_fa_btn
                            text: "Farsi"
                            size_hint_x: 0.5
                            on_release: app.set_audit_language("fa")
                    MDLabel:
                        text: "Auditor Name:"
                        font_style: "Caption"
                        adaptive_height: True
                    MDTextField:
                        id: audit_auditor
                        hint_text: "Enter auditor name"
                        mode: "rectangle"
                    MDLabel:
                        text: "Auditee / Section Name:"
                        font_style: "Caption"
                        adaptive_height: True
                    MDTextField:
                        id: audit_auditee
                        hint_text: "Enter auditee name"
                        mode: "rectangle"
                    MDLabel:
                        text: "Select Audit Section:"
                        font_style: "Subtitle1"
                        adaptive_height: True
                    MDRaisedButton:
                        id: audit_section_btn
                        text: "Select Section"
                        size_hint_x: 1
                        on_release: app.open_audit_section_menu()
                    MDRaisedButton:
                        text: "Start Audit"
                        pos_hint: {"center_x": 0.5}
                        on_release: app.start_audit()
                    Widget:
                        size_hint_y: None
                        height: "20dp"
    MDScreen:
        name: "audit_checklist"
        MDBoxLayout:
            orientation: "vertical"
            padding: "12dp"
            spacing: "8dp"
            MDBoxLayout:
                adaptive_height: True
                MDIconButton:
                    icon: "arrow-left"
                    on_release: app.go_to("audit")
                MDLabel:
                    id: audit_checklist_title
                    text: "Checklist"
                    font_style: "H5"
            ScrollView:
                MDBoxLayout:
                    id: audit_checklist_box
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: "10dp"
            MDRaisedButton:
                text: "Generate PDF Report"
                pos_hint: {"center_x": 0.5}
                on_release: app.generate_audit_pdf()
"""

class MehrLabApp(MDApp):
    RED = (0.95, 0.3, 0.3, 1)
    GREEN = (0.3, 0.85, 0.4, 1)
    GRAY = (0.7, 0.7, 0.7, 1)
    YELLOW = (0.95, 0.8, 0.2, 1)

    _display_cache = {}
    _analyte_cache = None

    def build(self):
        self.title = "Mehr Pathobiology Laboratory"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.current_detail_origin = "tests"
        self.unit_menu = None
        self.compare_menu = None
        self.audit_section_menu = None
        self.date_from_menu = None
        self.date_to_menu = None
        self.date_month_menu = None
        self.selected_analyte = None
        self.selected_from_unit = None
        self.selected_to_unit = None
        self.selected_critical_test = None
        self.critical_dialog = None
        self._search_event = None
        self._filter_event = None
        self.audit_auditor = ""
        self.audit_auditee = ""
        self.audit_selected_section = None
        self.audit_selected_section_finglish = ""
        self.audit_answers = {}
        self.audit_buttons = {}
        self.audit_language = "en"

        # Date converter state
        self.date_from_calendar = "jalali"
        self.date_to_calendar = "gregorian"
        self.date_month = None
        self.date_month_name = "Month"

        # Month names
        self.months_jalali = [
            "1 - Farvardin", "2 - Ordibehesht", "3 - Khordad",
            "4 - Tir", "5 - Mordad", "6 - Shahrivar",
            "7 - Mehr", "8 - Aban", "9 - Azar",
            "10 - Dey", "11 - Bahman", "12 - Esfand"
        ]
        self.months_gregorian = [
            "1 - January", "2 - February", "3 - March",
            "4 - April", "5 - May", "6 - June",
            "7 - July", "8 - August", "9 - September",
            "10 - October", "11 - November", "12 - December"
        ]
        self.months_hijri = [
            "1 - Muharram", "2 - Safar", "3 - Rabi al-Awwal",
            "4 - Rabi al-Thani", "5 - Jumada al-Awwal", "6 - Jumada al-Thani",
            "7 - Rajab", "8 - Sha'ban", "9 - Ramadan",
            "10 - Shawwal", "11 - Dhu al-Qi'dah", "12 - Dhu al-Hijjah"
        ]

        self.sm = Builder.load_string(KV)
        self.populate_tests()
        self.populate_converter_list()
        return self.sm

    def widget(self, widget_id):
        return self.sm.ids.get(widget_id)

    @staticmethod
    def fa_display(text):
        if not text:
            return ""
        reshaped = arabic_reshaper.reshape(str(text))
        return get_display(reshaped)

    def verify_login(self):
        pwd_field = self.widget("login_password")
        if not pwd_field:
            return
        if pwd_field.text.strip() == "848800":
            self.sm.current = "menu"
        else:
            dialog = MDDialog(
                title="Access Denied",
                text="Incorrect password. Please try again.",
                buttons=[MDFlatButton(text="OK", on_release=lambda x: dialog.dismiss())],
            )
            dialog.open()
            pwd_field.text = ""

    @classmethod
    def english_display(cls, value):
        import re
        key = str(value or "")
        if key in cls._display_cache:
            return cls._display_cache[key]
        text = key
        translations = {
            "قند ناشتا": "Fasting Blood Glucose", "خون": "Blood", "ادرار": "Urine",
            "کبد": "Liver", "کلیه": "Kidney", "چربی": "Lipid", "هورمون": "Hormone",
            "تیروئید": "Thyroid", "ویتامین": "Vitamin", "التهاب": "Inflammation",
            "الکترولیت": "Electrolyte", "میکروبیولوژی": "Microbiology", "عمومی": "General",
            "طبیعی": "Normal", "واحد": "Unit", "محدوده مرجع": "Reference Range",
            "توضیحات": "Notes",
        }
        for source, target in translations.items():
            text = text.replace(source, target)
        text = re.sub(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+", "", text)
        text = re.sub(r"\(\s*\)", "", text)
        text = re.sub(r"\s+", " ", text)
        result = text.strip()
        cls._display_cache[key] = result
        return result

    def get_test_names(self):
        return data.get_all_tests()

    def get_test_record(self, name):
        return data.get_test(name) or {}

    def find_test_name(self, query):
        query = (query or "").strip().casefold()
        if not query:
            return None
        for name in self.get_test_names():
            record = self.get_test_record(name)
            searchable = (name + " " + record.get("category", "")).casefold()
            if query in searchable:
                return name
        aliases = {
            "fbs": "Glucose", "bs": "Glucose", "tg": "Triglycerides",
            "creat": "Creatinine", "tbil": "Total Bilirubin", "dbil": "Direct Bilirubin",
            "ft4": "Free T4", "ft3": "Free T3", "tt4": "Total T4", "tt3": "Total T3",
            "hba1c": "HbA1c",
        }
        target = aliases.get(query)
        if target and data.get_test(target):
            return target
        return None

    def go_to(self, screen_name):
        self.sm.current = screen_name
        if screen_name == "tests":
            search = self.widget("all_tests_search")
            if search:
                search.text = ""
            self.populate_tests()
        elif screen_name == "search":
            search = self.widget("search_input")
            if search:
                search.text = ""
            self.clear_box("search_results")
        elif screen_name == "converter":
            self.populate_converter_list()
        elif screen_name == "critical":
            self.selected_critical_test = None
            btn = self.widget("crit_test_btn")
            if btn:
                btn.text = "Select Test"
            val = self.widget("crit_value")
            if val:
                val.text = ""
            res = self.widget("crit_result")
            if res:
                res.text = ""
        elif screen_name == "qc":
            for wid in ["qc_data1", "qc_x", "qc_y", "qc_mean", "qc_sd", "qc_cv"]:
                w = self.widget(wid)
                if w:
                    w.text = ""
            cmp_res = self.widget("qc_compare_result")
            if cmp_res:
                cmp_res.text = ""
        elif screen_name == "audit":
            self.audit_auditor = ""
            self.audit_auditee = ""
            self.audit_selected_section = None
            self.audit_selected_section_finglish = ""
            self.audit_answers = {}
            self.audit_buttons = {}
            for wid in ["audit_auditor", "audit_auditee"]:
                w = self.widget(wid)
                if w:
                    w.text = ""
            btn = self.widget("audit_section_btn")
            if btn:
                btn.text = "Select Section"
            box = self.widget("audit_checklist_box")
            if box:
                box.clear_widgets()
        elif screen_name == "date_converter":
            for wid in ["date_year", "date_day"]:
                w = self.widget(wid)
                if w:
                    w.text = ""
            res = self.widget("date_result")
            if res:
                res.text = ""
            self.date_from_calendar = "jalali"
            self.date_to_calendar = "gregorian"
            self.date_month = None
            self.date_month_name = "Month"
            btn_from = self.widget("date_from_btn")
            if btn_from:
                btn_from.text = "Jalali (Shamsi)"
            btn_to = self.widget("date_to_btn")
            if btn_to:
                btn_to.text = "Gregorian (Miladi)"
            btn_month = self.widget("date_month_btn")
            if btn_month:
                btn_month.text = "Month"

    def go_back_from_detail(self):
        self.go_to(self.current_detail_origin)

    def clear_box(self, widget_id):
        box = self.widget(widget_id)
        if box:
            box.clear_widgets()

    def search_tests_live(self, query):
        if self._search_event:
            self._search_event.cancel()
        self._search_event = Clock.schedule_once(lambda dt: self._do_search(query), 0.3)

    def _do_search(self, query):
        container = self.widget("search_results")
        if not container:
            return
        container.clear_widgets()
        query = (query or "").strip().casefold()
        if not query:
            return
        matches = data.search_tests(query)
        for name in matches[:50]:
            container.add_widget(OneLineListItem(
                text=self.english_display(name),
                on_release=lambda instance, n=name: self.show_test_detail(n, "search"),
            ))
        if not matches:
            container.add_widget(OneLineListItem(text="No matching tests found"))
        elif len(matches) > 50:
            container.add_widget(OneLineListItem(
                text=f"... and {len(matches) - 50} more. Refine your search."
            ))

    def filter_all_tests(self, query):
        if self._filter_event:
            self._filter_event.cancel()
        self._filter_event = Clock.schedule_once(lambda dt: self._do_filter_all(query), 0.2)

    def _do_filter_all(self, query):
        container = self.widget("all_tests_list")
        if not container:
            return
        container.clear_widgets()
        query = (query or "").strip().casefold()
        for name in self.get_test_names():
            record = self.get_test_record(name)
            category = record.get("category", "")
            shown_name = self.english_display(name)
            if (not query or query in name.casefold() or query in shown_name.casefold()
                    or query in category.casefold()):
                container.add_widget(OneLineListItem(
                    text=f"{shown_name}  |  {category}",
                    on_release=lambda instance, n=name: self.show_test_detail(n, "tests"),
                ))

    def populate_tests(self):
        self._do_filter_all("")

    def show_test_detail(self, test_name, origin="tests"):
        self.current_detail_origin = origin
        name_widget = self.widget("detail_name")
        info_widget = self.widget("detail_info")
        record = self.get_test_record(test_name)
        if name_widget:
            name_widget.text = self.english_display(test_name)
        units = record.get("units") or []
        default_unit = record.get("default_unit", "Not configured")
        sources = [
            ("CLIA", "clia_cva", "clia_tea", "clia_source"),
            ("Westgard", "westgard_cva", "westgard_tea", "westgard_source"),
            ("CLSI", "clsi_cva", "clsi_tea", "clsi_source"),
        ]
        lines = [
            f"Units: {', '.join(units) if units else 'Not configured'}",
            f"Default Unit: {default_unit}",
            "",
            "Allowable CVa / TEa (%):",
        ]
        has_any = False
        for label, cva_key, tea_key, src_key in sources:
            cva = record.get(cva_key)
            tea = record.get(tea_key)
            src = record.get(src_key) or ""
            if cva is None and tea is None and not src:
                continue
            has_any = True
            cva_txt = f"{cva:g}" if cva is not None else "—"
            tea_txt = f"{tea:g}" if tea is not None else "—"
            line = f"  • {label}: CVa = {cva_txt}  |  TEa = {tea_txt}"
            if src:
                line += f"\n      ({src})"
            lines.append(line)
        if not has_any:
            lines.append("  No CVa/TEa data recorded for this test.")
        if info_widget:
            info_widget.text = "\n".join(lines)
        self.sm.current = "detail"

    def set_label_color(self, label, color):
        if label:
            label.theme_text_color = "Custom"
            label.text_color = color

    def open_critical_test_picker(self):
        if self.critical_dialog:
            self.critical_dialog.dismiss()
        content = MDBoxLayout(orientation="vertical", spacing=dp(8),
                              size_hint_y=None, height=dp(420))
        search_field = MDTextField(hint_text="Type to filter tests...", mode="rectangle")
        content.add_widget(search_field)
        scroll = ScrollView()
        results_list = MDList()
        scroll.add_widget(results_list)
        content.add_widget(scroll)

        def refresh_results(query=""):
            results_list.clear_widgets()
            query = (query or "").strip().casefold()
            matches = data.search_tests(query) if query else data.get_all_tests()
            for name in matches[:60]:
                item = OneLineListItem(text=self.english_display(name))
                item.bind(on_release=lambda inst, n=name: pick(n))
                results_list.add_widget(item)
            if not matches:
                results_list.add_widget(OneLineListItem(text="No tests found"))

        def pick(name):
            self.selected_critical_test = name
            btn = self.widget("crit_test_btn")
            if btn:
                btn.text = f"Test: {self.english_display(name)}"
            if self.critical_dialog:
                self.critical_dialog.dismiss()

        search_field.bind(text=lambda inst, val: refresh_results(val))
        refresh_results("")
        self.critical_dialog = MDDialog(
            title="Select Test", type="custom", content_cls=content,
            buttons=[MDFlatButton(text="CANCEL",
                                  on_release=lambda x: self.critical_dialog.dismiss())],
        )
        self.critical_dialog.open()

    def check_critical_live(self):
        value_widget = self.widget("crit_value")
        result_widget = self.widget("crit_result")
        if not value_widget or not result_widget:
            return
        if not self.selected_critical_test:
            result_widget.text = "Please select a test first"
            self.set_label_color(result_widget, self.RED)
            return
        test_name = self.selected_critical_test
        try:
            value = float(value_widget.text)
        except (ValueError, TypeError):
            result_widget.text = "Enter a valid numeric result"
            self.set_label_color(result_widget, self.RED)
            return
        record = self.get_test_record(test_name)
        status = data.is_critical(test_name, value)
        unit = record.get("default_unit", "")
        source = record.get("critical_source") or (
            "Not documented; verify local laboratory policy")
        if status in ("LOW", "HIGH"):
            result_widget.text = (
                f"{self.english_display(test_name)}: CRITICAL {status} "
                f"({value:g} {unit})\nCritical limit source: {source}")
            self.set_label_color(result_widget, self.RED)
        elif status == "NORMAL":
            result_widget.text = (
                f"{self.english_display(test_name)}: Within configured critical limits")
            self.set_label_color(result_widget, self.GREEN)
        else:
            result_widget.text = (
                f"{self.english_display(test_name)}: Critical limits are not configured")
            self.set_label_color(result_widget, self.GRAY)

    @staticmethod
    def _parse_numbers(text):
        import re
        if not text:
            return []
        parts = re.split(r"[,;\s]+", text.strip())
        numbers = []
        for p in parts:
            if not p:
                continue
            try:
                numbers.append(float(p))
            except ValueError:
                continue
        return numbers

    def calculate_qc_stats(self):
        text1 = self.widget("qc_data1")
        if not text1:
            return
        values = self._parse_numbers(text1.text)
        mean_w = self.widget("qc_mean")
        sd_w = self.widget("qc_sd")
        cv_w = self.widget("qc_cv")
        if len(values) < 2:
            if mean_w: mean_w.text = "N/A"
            if sd_w: sd_w.text = "N/A"
            if cv_w: cv_w.text = "N/A"
            return
        n = len(values)
        mean = sum(values) / n
        variance = sum((x - mean) ** 2 for x in values) / (n - 1)
        sd = math.sqrt(variance)
        cv = (sd / mean * 100) if mean != 0 else 0
        if mean_w: mean_w.text = f"{mean:.4g}"
        if sd_w: sd_w.text = f"{sd:.4g}"
        if cv_w: cv_w.text = f"{cv:.2f}%"

    def open_qc_compare_menu(self):
        btn = self.widget("qc_cv")
        if not btn:
            return
        if self.compare_menu:
            self.compare_menu.dismiss()
        self.compare_menu = MDDropdownMenu(
            caller=btn,
            items=[
                {"text": "Linear Regression", "height": dp(48),
                 "on_release": lambda: self.run_compare("regression")},
                {"text": "F-test (Variance)", "height": dp(48),
                 "on_release": lambda: self.run_compare("ftest")},
            ],
            width_mult=4,
        )
        self.compare_menu.open()

    def run_compare(self, mode):
        if self.compare_menu:
            self.compare_menu.dismiss()
        t_x = self.widget("qc_x")
        t_y = self.widget("qc_y")
        res_w = self.widget("qc_compare_result")
        if not t_x or not t_y or not res_w:
            return
        x_vals = self._parse_numbers(t_x.text)
        y_vals = self._parse_numbers(t_y.text)
        if len(x_vals) < 2 or len(y_vals) < 2:
            res_w.text = "Both data sets need at least 2 values."
            self.set_label_color(res_w, self.RED)
            return
        if mode == "regression":
            self._run_regression(x_vals, y_vals, res_w)
        elif mode == "ftest":
            self._run_ftest(x_vals, y_vals, res_w)

    def _run_regression(self, x_vals, y_vals, res_w):
        n = min(len(x_vals), len(y_vals))
        x = x_vals[:n]
        y = y_vals[:n]
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        ss_xx = sum((xi - mean_x) ** 2 for xi in x)
        ss_yy = sum((yi - mean_y) ** 2 for yi in y)
        ss_xy = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        if ss_xx == 0:
            res_w.text = "Cannot compute regression: X has no variance."
            self.set_label_color(res_w, self.RED)
            return
        slope = ss_xy / ss_xx
        intercept = mean_y - slope * mean_x
        r = ss_xy / math.sqrt(ss_xx * ss_yy) if ss_yy > 0 else 0
        r2 = r * r
        ok = r2 >= 0.95
        res_w.text = (
            f"Regression (n={n}):\n"
            f"y = {slope:.4f}x + {intercept:.4f}\n"
            f"R² = {r2:.4f}  →  {'OK (strong linear relationship)' if ok else 'Weak linear relationship'}"
        )
        self.set_label_color(res_w, self.GREEN if ok else self.GRAY)

    def _run_ftest(self, x_vals, y_vals, res_w):
        n1, n2 = len(x_vals), len(y_vals)
        if n1 < 2 or n2 < 2:
            res_w.text = "Each data set needs at least 2 values for F-test."
            self.set_label_color(res_w, self.RED)
            return
        mean1 = sum(x_vals) / n1
        mean2 = sum(y_vals) / n2
        var1 = sum((v - mean1) ** 2 for v in x_vals) / (n1 - 1)
        var2 = sum((v - mean2) ** 2 for v in y_vals) / (n2 - 1)
        if var1 == 0 and var2 == 0:
            res_w.text = "Both variances are zero."
            self.set_label_color(res_w, self.GRAY)
            return
        if var1 >= var2:
            f_val = var1 / var2
            df_num, df_den = n1 - 1, n2 - 1
        else:
            f_val = var2 / var1
            df_num, df_den = n2 - 1, n1 - 1
        ok = f_val < 2.0
        res_w.text = (
            f"F-test (n1={n1}, n2={n2}):\n"
            f"Variance 1 = {var1:.6g}  |  Variance 2 = {var2:.6g}\n"
            f"F = {f_val:.4f} (df: {df_num}, {df_den})\n"
            f"→ {'Variances appear similar (OK)' if ok else 'Variances differ noticeably (check F-table)'}"
        )
        self.set_label_color(res_w, self.GREEN if ok else self.GRAY)

    def generate_qc_pdf(self):
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.lib.units import mm
            from reportlab.lib import colors
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.platypus import (
                SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
            )
            from reportlab.lib.enums import TA_CENTER
        except ImportError:
            self._show_toast("reportlab is not installed.")
            return

        mean_w = self.widget("qc_mean")
        sd_w = self.widget("qc_sd")
        cv_w = self.widget("qc_cv")
        cmp_w = self.widget("qc_compare_result")

        mean_txt = mean_w.text.strip() if mean_w else ""
        sd_txt = sd_w.text.strip() if sd_w else ""
        cv_txt = cv_w.text.strip() if cv_w else ""
        cmp_txt = cmp_w.text.strip() if cmp_w else ""

        if not mean_txt or mean_txt == "N/A":
            self._show_toast("Please calculate statistics first.")
            return

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"QC_Report_{timestamp}.pdf"
        abs_path = os.path.abspath(filename)

        try:
            doc = SimpleDocTemplate(
                abs_path,
                pagesize=A4,
                leftMargin=15 * mm,
                rightMargin=15 * mm,
                topMargin=15 * mm,
                bottomMargin=15 * mm,
            )
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(
                "Title", parent=styles["Title"], fontSize=16, alignment=TA_CENTER,
                spaceAfter=10,
            )
            h2_style = ParagraphStyle(
                "H2", parent=styles["Heading2"], fontSize=12, spaceBefore=10, spaceAfter=6,
            )
            normal_style = ParagraphStyle(
                "Normal", parent=styles["Normal"], fontSize=9, leading=12,
            )

            story = []
            story.append(Paragraph("Mehr Pathobiology Laboratory", title_style))
            story.append(Paragraph(
                "Prepared by: Mehran Mohammadi",
                ParagraphStyle("Subtitle", parent=normal_style, fontSize=10,
                               alignment=TA_CENTER, textColor=colors.grey),
            ))
            story.append(Spacer(1, 6))
            story.append(Paragraph("QC Statistics Report", h2_style))
            story.append(Spacer(1, 8))
            story.append(Paragraph(
                f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
                normal_style,
            ))
            story.append(Spacer(1, 12))

            story.append(Paragraph("Statistics", h2_style))
            stats_data = [
                ["Parameter", "Value"],
                ["Mean", mean_txt],
                ["SD", sd_txt],
                ["CV%", cv_txt],
            ]
            stats_table = Table(stats_data, colWidths=[60 * mm, 60 * mm])
            stats_table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#00796B")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("GRID", (0, 0), (-1, -1), 0.3, colors.grey),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
            ]))
            story.append(stats_table)
            story.append(Spacer(1, 12))

            if cmp_txt:
                story.append(Paragraph("Comparison Result", h2_style))
                for line in cmp_txt.split("\n"):
                    story.append(Paragraph(line, normal_style))
                story.append(Spacer(1, 12))

            story.append(Spacer(1, 20))
            story.append(Paragraph(
                "This report was generated by Mehr Pathobiology Laboratory application.",
                ParagraphStyle("Footer", parent=normal_style, fontSize=8,
                               textColor=colors.grey, alignment=TA_CENTER),
            ))

            doc.build(story)
            self._open_pdf(abs_path)

        except Exception as e:
            self._show_toast(f"Error generating PDF:\n{str(e)}")

    # ==================================================
    # DATE CONVERTER
    # ==================================================
    def open_date_month_menu(self):
        btn = self.widget("date_month_btn")
        if not btn:
            return
        if self.date_month_menu:
            self.date_month_menu.dismiss()
        
        # انتخاب لیست ماه‌ها بر اساس تقویم مبدأ
        if self.date_from_calendar == "jalali":
            months = self.months_jalali
        elif self.date_from_calendar == "gregorian":
            months = self.months_gregorian
        else:  # hijri
            months = self.months_hijri

        self.date_month_menu = MDDropdownMenu(
            caller=btn,
            items=[
                {"text": m, "height": dp(48),
                 "on_release": lambda sel=m: self.set_date_month(sel)}
                for m in months
            ],
            width_mult=4,
        )
        self.date_month_menu.open()

    def set_date_month(self, month_str):
        # جدا کردن شماره از نام (مثلاً "7 - Mehr" -> شماره 7)
        num = int(month_str.split(" - ")[0])
        self.date_month = num
        self.date_month_name = month_str
        btn = self.widget("date_month_btn")
        if btn:
            btn.text = month_str
        if self.date_month_menu:
            self.date_month_menu.dismiss()

    def open_date_from_menu(self):
        btn = self.widget("date_from_btn")
        if not btn:
            return
        if self.date_from_menu:
            self.date_from_menu.dismiss()
        self.date_from_menu = MDDropdownMenu(
            caller=btn,
            items=[
                {"text": "Jalali (Shamsi)", "height": dp(48),
                 "on_release": lambda: self.set_date_from("jalali", "Jalali (Shamsi)")},
                {"text": "Gregorian (Miladi)", "height": dp(48),
                 "on_release": lambda: self.set_date_from("gregorian", "Gregorian (Miladi)")},
                {"text": "Hijri (Ghamari)", "height": dp(48),
                 "on_release": lambda: self.set_date_from("hijri", "Hijri (Ghamari)")},
            ],
            width_mult=4,
        )
        self.date_from_menu.open()

    def set_date_from(self, calendar, label):
        self.date_from_calendar = calendar
        self.date_month = None
        self.date_month_name = "Month"
        btn = self.widget("date_from_btn")
        if btn:
            btn.text = label
        btn_month = self.widget("date_month_btn")
        if btn_month:
            btn_month.text = "Month"
        if self.date_from_menu:
            self.date_from_menu.dismiss()

    def open_date_to_menu(self):
        btn = self.widget("date_to_btn")
        if not btn:
            return
        if self.date_to_menu:
            self.date_to_menu.dismiss()
        self.date_to_menu = MDDropdownMenu(
            caller=btn,
            items=[
                {"text": "Jalali (Shamsi)", "height": dp(48),
                 "on_release": lambda: self.set_date_to("jalali", "Jalali (Shamsi)")},
                {"text": "Gregorian (Miladi)", "height": dp(48),
                 "on_release": lambda: self.set_date_to("gregorian", "Gregorian (Miladi)")},
                {"text": "Hijri (Ghamari)", "height": dp(48),
                 "on_release": lambda: self.set_date_to("hijri", "Hijri (Ghamari)")},
            ],
            width_mult=4,
        )
        self.date_to_menu.open()

    def set_date_to(self, calendar, label):
        self.date_to_calendar = calendar
        btn = self.widget("date_to_btn")
        if btn:
            btn.text = label
        if self.date_to_menu:
            self.date_to_menu.dismiss()

    def do_date_convert(self):
        result_widget = self.widget("date_result")
        year_w = self.widget("date_year")
        day_w = self.widget("date_day")

        if not all([year_w, day_w, result_widget]):
            return

        if self.date_month is None:
            result_widget.text = "Please select a month."
            self.set_label_color(result_widget, self.RED)
            return

        try:
            year = int(year_w.text)
            day = int(day_w.text)
            month = self.date_month
        except (ValueError, TypeError):
            result_widget.text = "Please enter valid numbers for year and day."
            self.set_label_color(result_widget, self.RED)
            return

        try:
            from waxt import DateTime
        except ImportError:
            result_widget.text = "waxt library is not installed. Run: pip install waxt"
            self.set_label_color(result_widget, self.RED)
            return

        try:
            source_date = DateTime(year, month, day, calendar=self.date_from_calendar)
            target_date = source_date.to_calendar(self.date_to_calendar)
            
            result_widget.text = f"{target_date.year}/{target_date.month:02d}/{target_date.day:02d}"
            self.set_label_color(result_widget, self.GREEN)
        except Exception as e:
            result_widget.text = f"Conversion error: {str(e)}"
            self.set_label_color(result_widget, self.RED)

    # ==================================================
    # INTERNAL AUDIT
    # ==================================================
    def open_audit_section_menu(self):
        btn = self.widget("audit_section_btn")
        if not btn:
            return
        if self.audit_section_menu:
            self.audit_section_menu.dismiss()
        
        menu_items = []
        if self.audit_language == "fa":
            menu_items.append({
                "text": "Momi",
                "height": dp(48),
                "on_release": lambda s="ممیزی", f="Momi": self.select_audit_section(s, f)
            })
        else:
            sections = list(audit_data.AUDIT_SECTIONS_EN.keys())
            for sec in sections:
                menu_items.append({
                    "text": sec,
                    "height": dp(48),
                    "on_release": lambda s=sec, f=sec: self.select_audit_section(s, f)
                })

        self.audit_section_menu = MDDropdownMenu(
            caller=btn,
            items=menu_items,
            width_mult=4,
        )
        self.audit_section_menu.open()

    def select_audit_section(self, section, finglish_name):
        self.audit_selected_section = section
        self.audit_selected_section_finglish = finglish_name
        btn = self.widget("audit_section_btn")
        if btn:
            if self.audit_language == "fa":
                btn.text = f"Bakhsh: {section}"
            else:
                btn.text = f"Section: {section}"
        if self.audit_section_menu:
            self.audit_section_menu.dismiss()

    def set_audit_language(self, lang):
        self.audit_language = lang
        en_btn = self.widget("lang_en_btn")
        fa_btn = self.widget("lang_fa_btn")
        if lang == "en":
            if en_btn: en_btn.md_bg_color = (0.0, 0.5, 0.5, 1)
            if fa_btn: fa_btn.md_bg_color = (0.3, 0.3, 0.3, 1)
        else:
            if en_btn: en_btn.md_bg_color = (0.3, 0.3, 0.3, 1)
            if fa_btn: fa_btn.md_bg_color = (0.0, 0.5, 0.5, 1)

    def start_audit(self):
        auditor_w = self.widget("audit_auditor")
        auditee_w = self.widget("audit_auditee")
        self.audit_auditor = auditor_w.text.strip() if auditor_w else ""
        self.audit_auditee = auditee_w.text.strip() if auditee_w else ""

        if not self.audit_auditor:
            self._show_toast("Please enter auditor name")
            return
        if not self.audit_auditee:
            self._show_toast("Please enter auditee name")
            return
        if not self.audit_selected_section:
            self._show_toast("Please select an audit section")
            return

        self.audit_answers = {}
        self.audit_buttons = {}
        self.show_audit_checklist()

    def _show_toast(self, message):
        dialog = MDDialog(
            title="Notice",
            text=message,
            buttons=[MDFlatButton(text="OK", on_release=lambda x: dialog.dismiss())],
        )
        dialog.open()

    def show_audit_checklist(self):
        title_w = self.widget("audit_checklist_title")
        box = self.widget("audit_checklist_box")
        if not box:
            return
        if title_w:
            if self.audit_language == "fa":
                title_w.text = self.fa_display(f"چک‌لیست: {self.audit_selected_section}")
            else:
                title_w.text = f"Checklist: {self.audit_selected_section}"
        box.clear_widgets()

        if self.audit_language == "fa":
            questions = audit_data.AUDIT_SECTIONS_FA.get(self.audit_selected_section, [])
        else:
            questions = audit_data.AUDIT_SECTIONS_EN.get(self.audit_selected_section, [])

        from kivymd.uix.card import MDCard
        from kivy.uix.boxlayout import BoxLayout

        self.audit_buttons = {}

        for idx, q in enumerate(questions):
            card = MDCard(
                orientation="vertical",
                padding=dp(10),
                spacing=dp(6),
                size_hint_y=None,
                height=dp(160),
                radius=[dp(8)],
                elevation=2,
            )
            display_q = self.fa_display(q) if self.audit_language == "fa" else q
            
            q_label = PersianMDLabel(
                text=f"{idx + 1}. {display_q}",
                font_style="Caption",
                adaptive_height=True,
                size_hint_y=None,
            )
            q_label.height = max(q_label.texture_size[1], dp(40))
            card.add_widget(q_label)

            btn_row = BoxLayout(
                orientation="horizontal",
                size_hint_y=None,
                height=dp(40),
                spacing=dp(4),
            )

            current = self.audit_answers.get(q, None)
            self.audit_buttons[q] = {}

            def make_handler(question, answer):
                def handler(inst):
                    self.audit_answers[question] = answer
                    self._update_audit_button_colors(question)
                return handler

            if self.audit_language == "fa":
                btn_labels = [
                    ("بله", "yes", (0.2, 0.7, 0.3, 1), (0.3, 0.3, 0.3, 1)),
                    ("خیر", "no", (0.8, 0.2, 0.2, 1), (0.3, 0.3, 0.3, 1)),
                    ("نیاز به اقدام", "action", (0.9, 0.7, 0.1, 1), (0.3, 0.3, 0.3, 1)),
                ]
            else:
                btn_labels = [
                    ("Yes", "yes", (0.2, 0.7, 0.3, 1), (0.3, 0.3, 0.3, 1)),
                    ("No", "no", (0.8, 0.2, 0.2, 1), (0.3, 0.3, 0.3, 1)),
                    ("Action Needed", "action", (0.9, 0.7, 0.1, 1), (0.3, 0.3, 0.3, 1)),
                ]

            for label, ans, color_on, color_off in btn_labels:
                btn = PersianMDRaisedButton(
                    text=self.fa_display(label) if self.audit_language == "fa" else label,
                    size_hint_x=0.33,
                    md_bg_color=color_on if current == ans else color_off,
                )
                btn.bind(on_release=make_handler(q, ans))
                btn_row.add_widget(btn)
                self.audit_buttons[q][ans] = (btn, color_on, color_off)

            card.add_widget(btn_row)
            box.add_widget(card)

        self.sm.current = "audit_checklist"

    def _update_audit_button_colors(self, question):
        if not hasattr(self, "audit_buttons") or question not in self.audit_buttons:
            return
        current = self.audit_answers.get(question, None)
        for ans, (btn, color_on, color_off) in self.audit_buttons[question].items():
            btn.md_bg_color = color_on if current == ans else color_off

    def generate_audit_pdf(self):
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.lib.units import mm
            from reportlab.lib import colors
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.platypus import (
                SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
            )
            from reportlab.lib.enums import TA_CENTER, TA_RIGHT
        except ImportError:
            self._show_toast("reportlab is not installed.")
            return

        if not self.audit_auditor or not self.audit_auditee or not self.audit_selected_section:
            self._show_toast("Please complete all audit fields first.")
            return

        if self.audit_language == "fa":
            questions = audit_data.AUDIT_SECTIONS_FA.get(self.audit_selected_section, [])
        else:
            questions = audit_data.AUDIT_SECTIONS_EN.get(self.audit_selected_section, [])
            
        if not questions:
            self._show_toast("No questions found for this section.")
            return

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_section = "".join(c if c.isalnum() else "_" for c in self.audit_selected_section_finglish)
        filename = f"Audit_Report_{safe_section}_{timestamp}.pdf"
        abs_path = os.path.abspath(filename)

        try:
            doc = SimpleDocTemplate(
                abs_path,
                pagesize=A4,
                leftMargin=15 * mm,
                rightMargin=15 * mm,
                topMargin=15 * mm,
                bottomMargin=15 * mm,
            )
            styles = getSampleStyleSheet()
            
            title_style = ParagraphStyle(
                "Title", parent=styles["Title"], fontName="Vazir", fontSize=16, alignment=TA_CENTER,
                spaceAfter=10,
            )
            h2_style = ParagraphStyle(
                "H2", parent=styles["Heading2"], fontName="Vazir", fontSize=12, spaceBefore=10, spaceAfter=6,
            )
            normal_style = ParagraphStyle(
                "Normal", parent=styles["Normal"], fontName="Vazir", fontSize=9, leading=12,
            )
            
            cell_style_fa = ParagraphStyle(
                "CellFa", parent=styles["Normal"], fontName="Vazir", fontSize=8, leading=10, alignment=TA_RIGHT,
            )
            cell_style_en = ParagraphStyle(
                "CellEn", parent=styles["Normal"], fontName="Vazir", fontSize=8, leading=10,
            )
            
            cell_style = cell_style_fa if self.audit_language == "fa" else cell_style_en

            story = []
            story.append(Paragraph("Mehr Pathobiology Laboratory", title_style))
            story.append(Paragraph(
                "Prepared by: Mehran Mohammadi",
                ParagraphStyle("Subtitle", parent=normal_style, fontName="Vazir", fontSize=10,
                               alignment=TA_CENTER, textColor=colors.grey),
            ))
            story.append(Spacer(1, 6))
            story.append(Paragraph("Internal Audit Report", h2_style))
            story.append(Paragraph(
                "Reference Standard: ISO 15189:2022 / Iranian Lab Regulations 1398",
                ParagraphStyle("Ref", parent=normal_style, fontName="Vazir", fontSize=9,
                               alignment=TA_CENTER),
            ))
            story.append(Spacer(1, 8))

            info_data = [
                [Paragraph("Auditor:", normal_style), Paragraph(self.audit_auditor, normal_style)],
                [Paragraph("Auditee / Section:", normal_style), Paragraph(self.audit_auditee, normal_style)],
                [Paragraph("Audit Section:", normal_style), Paragraph(self.audit_selected_section_finglish, normal_style)],
                [Paragraph("Date:", normal_style), Paragraph(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), normal_style)],
            ]
            info_table = Table(info_data, colWidths=[45 * mm, 120 * mm])
            info_table.setStyle(TableStyle([
                ("FONTNAME", (0, 0), (-1, -1), "Vazir"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]))
            story.append(info_table)
            story.append(Spacer(1, 12))

            story.append(Paragraph("Audit Checklist", h2_style))
            
            if self.audit_language == "fa":
                headers = [
                    Paragraph("جواب", normal_style), 
                    Paragraph("سوال", normal_style), 
                    Paragraph("#", normal_style)
                ]
                rows = [headers]
                for idx, q in enumerate(questions):
                    ans = self.audit_answers.get(q, "")
                    if ans == "yes":
                        result = self.fa_display("بله")
                    elif ans == "no":
                        result = self.fa_display("خیر")
                    elif ans == "action":
                        result = self.fa_display("نیاز به اقدام")
                    else:
                        result = "-"
                    
                    display_q = self.fa_display(q)
                    
                    rows.append([
                        Paragraph(result, cell_style),
                        Paragraph(display_q, cell_style),
                        Paragraph(str(idx + 1), cell_style),
                    ])
                col_widths = [25 * mm, 130 * mm, 10 * mm]
            else:
                headers = [
                    Paragraph("#", normal_style), 
                    Paragraph("Question", normal_style), 
                    Paragraph("Result", normal_style)
                ]
                rows = [headers]
                for idx, q in enumerate(questions):
                    ans = self.audit_answers.get(q, "")
                    if ans == "yes":
                        result = "Yes"
                    elif ans == "no":
                        result = "No"
                    elif ans == "action":
                        result = "Action Needed"
                    else:
                        result = "-"
                    
                    rows.append([
                        Paragraph(str(idx + 1), cell_style),
                        Paragraph(q, cell_style),
                        Paragraph(result, cell_style),
                    ])
                col_widths = [10 * mm, 130 * mm, 25 * mm]

            yes_count = no_count = action_count = 0
            for q in questions:
                ans = self.audit_answers.get(q, "")
                if ans == "yes": yes_count += 1
                elif ans == "no": no_count += 1
                elif ans == "action": action_count += 1

            table = Table(rows, colWidths=col_widths, repeatRows=1)
            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#00796B")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, -1), "Vazir"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("GRID", (0, 0), (-1, -1), 0.3, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F5F5F5")]),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
            ]))
            story.append(table)

            story.append(Spacer(1, 12))
            story.append(Paragraph("Summary", h2_style))
            
            summary_data = [
                [Paragraph("Total Questions:", normal_style), Paragraph(str(len(questions)), normal_style)],
                [Paragraph("Yes (Compliant):", normal_style), Paragraph(str(yes_count), normal_style)],
                [Paragraph("No (Non-compliant):", normal_style), Paragraph(str(no_count), normal_style)],
                [Paragraph("Action Needed:", normal_style), Paragraph(str(action_count), normal_style)],
                [Paragraph("Unanswered:", normal_style), Paragraph(str(len(questions) - yes_count - no_count - action_count), normal_style)],
            ]
            summary_table = Table(summary_data, colWidths=[60 * mm, 40 * mm])
            summary_table.setStyle(TableStyle([
                ("FONTNAME", (0, 0), (-1, -1), "Vazir"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("GRID", (0, 0), (-1, -1), 0.3, colors.grey),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]))
            story.append(summary_table)

            story.append(Spacer(1, 20))
            story.append(Paragraph(
                "This report was generated by Mehr Pathobiology Laboratory application.",
                ParagraphStyle("Footer", parent=normal_style, fontName="Vazir", fontSize=8,
                               textColor=colors.grey, alignment=TA_CENTER),
            ))

            doc.build(story)
            self._open_pdf(abs_path)

        except Exception as e:
            self._show_toast(f"Error generating PDF:\n{str(e)}")

    def _open_pdf(self, path):
        import sys
        if sys.platform == "android":
            try:
                from androidstorage4kivy import SharedStorage, ShareSheet
                shared = SharedStorage()
                shared_file = shared.copy_to_shared(path)
                if shared_file:
                    sheet = ShareSheet()
                    sheet.view_file(shared_file)
                else:
                    self._show_toast("Could not copy PDF to shared storage.")
            except Exception as e:
                self._show_toast(f"Error opening PDF on Android:\n{str(e)}")
            return

        try:
            if sys.platform.startswith("win"):
                os.startfile(path)
            elif sys.platform == "darwin":
                os.system(f'open "{path}"')
            else:
                os.system(f'xdg-open "{path}"')
        except Exception as e:
            self._show_toast(f"PDF created but could not open:\n{path}\n\n{str(e)}")

    def populate_converter_list(self):
        container = self.widget("conv_list")
        if not container:
            return
        container.clear_widgets()
        for source, target in converter.list_conversions():
            container.add_widget(OneLineListItem(text=f"{source}  ->  {target}"))

    def get_analyte_options(self):
        if self._analyte_cache is not None:
            return self._analyte_cache
        options = []
        for name in data.get_all_tests():
            units = converter.units_for_analyte(name)
            if len(units) >= 2:
                options.append(name)
        result = ["General Conversion"] + sorted(set(options), key=str.casefold)
        self.__class__._analyte_cache = result
        return result

    def get_current_units(self):
        if self.selected_analyte:
            units = converter.units_for_analyte(self.selected_analyte)
            if units:
                return units
        return converter.list_general_units()

    def open_unit_menu(self, side):
        if side == "analyte":
            button = self.widget("conv_analyte")
            options = self.get_analyte_options()
        elif side == "from":
            button = self.widget("conv_from")
            options = self.get_current_units()
        else:
            button = self.widget("conv_to")
            options = self.get_current_units()
        if not button or not options:
            return
        if self.unit_menu:
            self.unit_menu.dismiss()
        self.unit_menu = MDDropdownMenu(
            caller=button,
            items=[{"text": option, "height": dp(48),
                    "on_release": lambda selected=option, s=side: self.select_unit(s, selected)}
                   for option in options],
            width_mult=4,
        )
        self.unit_menu.open()

    def select_unit(self, side, selected):
        if side == "analyte":
            analyte_button = self.widget("conv_analyte")
            from_button = self.widget("conv_from")
            to_button = self.widget("conv_to")
            if selected == "General Conversion":
                self.selected_analyte = None
                self.selected_from_unit = None
                self.selected_to_unit = None
                if analyte_button: analyte_button.text = "General Conversion"
                if from_button: from_button.text = "From Unit"
                if to_button: to_button.text = "To Unit"
            else:
                self.selected_analyte = selected
                if analyte_button: analyte_button.text = f"Analyte: {selected}"
                units = converter.units_for_analyte(selected)
                self.selected_from_unit = units[0] if units else None
                self.selected_to_unit = units[1] if len(units) > 1 else None
                if from_button: from_button.text = self.selected_from_unit or "From Unit"
                if to_button: to_button.text = self.selected_to_unit or "To Unit"
        elif side == "from":
            self.selected_from_unit = selected
            button = self.widget("conv_from")
            if button: button.text = selected
        elif side == "to":
            self.selected_to_unit = selected
            button = self.widget("conv_to")
            if button: button.text = selected
        if self.unit_menu:
            self.unit_menu.dismiss()

    def do_convert(self):
        value_widget = self.widget("conv_value")
        result_widget = self.widget("conv_result")
        if not value_widget or not result_widget:
            return
        try:
            value = float(value_widget.text)
        except (ValueError, TypeError):
            result_widget.text = "Enter a valid numeric value"
            self.set_label_color(result_widget, self.RED)
            return
        source = self.selected_from_unit
        target = self.selected_to_unit
        if not source or not target:
            result_widget.text = "Select both units first"
            self.set_label_color(result_widget, self.RED)
            return
        result = converter.convert(value, source, target, analyte=self.selected_analyte)
        if result is None:
            result_widget.text = "Unsupported conversion for this analyte and unit pair"
            self.set_label_color(result_widget, self.RED)
            return
        result_widget.text = f"{value:g} {source} = {result:.6g} {target}"
        self.set_label_color(result_widget, self.GREEN)

if __name__ == "__main__":
    MehrLabApp().run()
