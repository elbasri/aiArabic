import numpy as np
import plotly.graph_objects as go

# توليد بيانات افتراضية (عدد ساعات الدراسة والنتائج)
np.random.seed(42)
ساعات_الدراسة = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
النتائج = np.array([50, 55, 60, 63, 67, 70, 74, 78, 82, 85]) + np.random.normal(0, 2, 10)

# حساب معادلة الانحدار الخطي
م, ج = np.polyfit(ساعات_الدراسة, النتائج, 1)

# إنشاء القيم المتوقعة للخط
خط_الانحدار = م * ساعات_الدراسة + ج

# توليد نقطة جديدة للتنبؤ
نقطة_جديدة = 11
توقع_جديد = م * نقطة_جديدة + ج

# إنشاء الرسم البياني
fig = go.Figure()

# إضافة النقاط الفعلية
fig.add_trace(go.Scatter(x=ساعات_الدراسة, y=النتائج, mode='markers',
                         marker=dict(size=8, color='blue'),
                         name="البيانات الفعلية"))

# إضافة خط الانحدار
fig.add_trace(go.Scatter(x=ساعات_الدراسة, y=خط_الانحدار, mode='lines',
                         line=dict(color='red', width=2),
                         name="خط الانحدار الخطي"))

# إضافة نقطة التنبؤ الجديدة
fig.add_trace(go.Scatter(x=[نقطة_جديدة], y=[توقع_جديد], mode='markers',
                         marker=dict(size=10, color='green', symbol='star'),
                         name="قيمة متوقعة جديدة"))


# إضافة ملاحظة لحفظ الحقوق
annotation = dict(
    x=min(ساعات_الدراسة),
    y=min(النتائج),
    text="www.nacer.ma",
    showarrow=False,
    xanchor="left",
    yanchor="bottom",
    font=dict(size=12, color="gray")
)

# تخصيص العنوان والمحاور
fig.update_layout(
    title="الانحدار الخطي: العلاقة بين ساعات الدراسة والنتائج",
    xaxis_title="عدد ساعات الدراسة",
    yaxis_title="النتيجة في الامتحان",
    template="plotly_white",
    annotations=[
        dict(x=8, y=81, text="ص= م∗س + ج", showarrow=False, font=dict(size=16, color="black")),
        dict(x=8, y=77, text="Y = mX + b", showarrow=False, font=dict(size=16, color="black")),
        dict(x=نقطة_جديدة, y=توقع_جديد, text="🔮 توقع جديد", showarrow=True, arrowhead=3, ax=30, ay=-40, font=dict(size=14)),
        annotation
    ]
)

# إضافة العلامة المائية
fig.add_annotation(
    xref="paper", yref="paper",
    x=0.01, y=-0.15,
    text="www.nacer.ma",
    showarrow=False,
    font=dict(size=14, color="gray")
)

# عرض الرسم البياني
fig.show()
