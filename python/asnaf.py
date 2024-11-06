# الأصناف والكائنات هي أساس البرمجة الكائنية التي تعتبر أحد أكثر الأنماط الأمرية شيوعا
# الصنف هو قالب أو مخطط يتم من خلاله إنشاء الكائنات التي تتشارك خصائص وسلوكيات معينة
    # معجم:
    ## صنف = class
    ## كائن = object

# مثال:
# تعريف صنف
class Montaj:
    # هذه دالة خاصة ضمن ما يسمى بالتوابع
    # هذا بالذات يسمى بالتابع الباني ويستدعى في كل مرة يتم إنشاء نسخة من الصنف
    # هذه خاصية مشتركة
    no3 = "HATIF"
    # ويأخذ عدة عوامل كما هو في مثالنا هذا
    def __init__(self, id, ism, wasf, taman, majmo3):
        # أما الأول فهو يشير للكائن نفسه
        # أما البقية فهي طريق الحصول على قيم الخصائص الخارجية التي سيحصل عليها الصنف، لذلك نضيفها له هكذا:
        self.id = id
        self.ism = ism
        self.wasf = wasf
        self.taman = taman
        self.majmo3 = majmo3

    def takhfid(self, khasya, kima):
        if khasya == "taman" : 
            self.taman = self.taman - float(kima)
        else:
            self.majmo3 = self.majmo3 - int(kima)
    
# إنشاء كائنات 
iphone_15 = Montaj(id = 1, ism = "أيفون 15", wasf = "هاتف التفاحة الشهير", taman = 13000 , majmo3 = 5)
sumsung_s24 = Montaj(id = 2, ism = "سامسونج إس 24", wasf = "الكوري العنيد", taman = 12000 , majmo3 = 7)

# طبع نوع المتغيرين/الكائنين
print(iphone_15)
print(sumsung_s24)
# نلاحظ اختلاف المعرفين للمتغيرين من نفس الصنف، وذلك لكون الكائنين مختلفين حقيقة.


# طبع الخاصية المشتركة
print(iphone_15.no3)
print(sumsung_s24.no3)

# طبع خواص أخرى
print(iphone_15.taman)
print(sumsung_s24.majmo3)

# تعديل قيم الخاصيات
iphone_15.takhfid("taman", 507.5)
sumsung_s24.takhfid("majmo3", 2)


# طبع نفس الخواص بعد التعديل
print(iphone_15.taman)
print(sumsung_s24.majmo3)