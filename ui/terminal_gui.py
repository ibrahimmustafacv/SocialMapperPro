#!/usr/bin/env python3
"""
واجهة الترمنال المتقدمة - SocialMapper Pro
"""

import os
import time
from colorama import Fore, Style, init

init(autoreset=True)

class MainInterface:
    def __init__(self):
        self.version = "2.0.0"
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def show_banner(self):
        self.clear_screen()
        banner = f"""
{Fore.CYAN}
███████ ██████  ██████  ███████ ███████ ███    ███ 
██      ██   ██ ██   ██ ██      ██      ████  ████ 
███████ ██████  ██████  █████   █████   ██ ████ ██ 
     ██ ██      ██   ██ ██      ██      ██  ██  ██ 
███████ ██      ██   ██ ███████ ███████ ██      ██ 
{Style.RESET_ALL}
{Fore.YELLOW}🚀 SocialMapper Pro v{self.version}
{Fore.RED}⚠️  FOR EDUCATIONAL USE ONLY
"""
        print(banner)
    
    def main_menu(self):
        print(f"""
{Fore.CYAN}1.{Fore.WHITE} فيسبوك إنتليجنس
{Fore.CYAN}2.{Fore.WHITE} انستجرام إنتليجنس {Fore.RED}[قيد التطوير]
{Fore.CYAN}3.{Fore.WHITE} إعدادات النظام
{Fore.CYAN}4.{Fore.WHITE} خروج

{Fore.GREEN}اختر الخيار [1-4]: {Style.RESET_ALL}""")
        return input().strip()
    
    def facebook_menu(self):
        self.clear_screen()
        print(f"""
{Fore.CYAN}1.{Fore.WHITE} البحث عن الأبناء من اسم الأب
{Fore.CYAN}2.{Fore.WHITE} البحث عن شخص معين  
{Fore.CYAN}3.{Fore.WHITE} العودة للقائمة الرئيسية

{Fore.GREEN}اختر الخيار [1-3]: {Style.RESET_ALL}""")
        return input().strip()
    
    def get_facebook_target(self):
        print(f"\n{Fore.CYAN}🎯 إدخال بيانات الهدف{Style.RESET_ALL}")
        url = input(f"{Fore.YELLOW}رابط الفيسبوك: {Style.RESET_ALL}").strip()
        return {'url': url}
    
    def get_father_name(self):
        return input(f"{Fore.YELLOW}اسم الأب: {Style.RESET_ALL}").strip()
    
    def get_username(self):
        return input(f"{Fore.YELLOW}اسم المستخدم: {Style.RESET_ALL}").strip()
    
    def show_scan_progress(self, message):
        print(f"\n{Fore.YELLOW}⏳ {message}{Style.RESET_ALL}")
    
    def update_progress(self, progress, message):
        print(f"{Fore.CYAN}📊 {progress}% - {message}{Style.RESET_ALL}")
    
    def show_results_summary(self, results, report_path):
        print(f"\n{Fore.GREEN}✅ تم العثور على {len(results)} نتيجة{Style.RESET_ALL}")
        print(f"{Fore.CYAN}💾 التقرير: {report_path}{Style.RESET_ALL}")
        
        for result in results:
            print(f"{Fore.WHITE}• {result['name']} - {result['url']}{Style.RESET_ALL}")
        
        input(f"\n{Fore.GREEN}اضغط Enter للمتابعة...{Style.RESET_ALL}")
    
    def show_message(self, msg_type, message):
        colors = {'success': Fore.GREEN, 'error': Fore.RED, 'warning': Fore.YELLOW, 'info': Fore.CYAN}
        icons = {'success': '✅', 'error': '❌', 'warning': '⚠️', 'info': 'ℹ️'}
        
        color = colors.get(msg_type, Fore.WHITE)
        icon = icons.get(msg_type, '📌')
        print(f"{color}{icon} {message}{Style.RESET_ALL}")