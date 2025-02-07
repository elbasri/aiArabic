import numpy as np
import plotly.graph_objects as go

# بيانات افتراضية (عدد ساعات الدراسة والنتائج)
ساعات_الدراسة = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
النتائج = np.array([50, 55, 60, 63, 67, 70, 74, 78, 82, 85])

# حساب معادلة الانحدار الخطي
م, ج = np.polyfit(ساعات_الدراسة, النتائج, 1)

# إنشاء النقاط الفعلية
scatter = go.Scatter(
    x=ساعات_الدراسة,
    y=النتائج,
    mode='markers',
    marker=dict(color='blue'),
    name='البيانات الفعلية'
)

# إنشاء خط الانحدار الخطي
line = go.Scatter(
    x=ساعات_الدراسة,
    y=م * ساعات_الدراسة + ج,
    mode='lines',
    line=dict(color='red'),
    name='خط الانحدار الخطي'
)

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

# إنشاء الشكل
fig = go.Figure(data=[scatter, line])

# تخصيص التصميم
fig.update_layout(
    title="العلاقة بين عدد ساعات الدراسة والنتائج",
    xaxis_title="عدد ساعات الدراسة",
    yaxis_title="النتيجة في الامتحان",
    annotations=[annotation]
)

# عرض الرسم البياني
fig.show()
